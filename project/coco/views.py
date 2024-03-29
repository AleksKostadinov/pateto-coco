import os
import requests
import folium
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, PlacesVisited
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from random import choice
from .forms import CommentForm, SubscribersForm, MailMessageForm
from newsapi import NewsApiClient
from decouple import config


def get_recent_posts():
    return Post.objects.filter(status='Published')[:6]


def get_random_pinned_post():
    pinned_posts = Post.objects.filter(pinned=True, status='Published')
    return choice(pinned_posts) if pinned_posts else None


def home(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = SubscribersForm()

    last_posts = get_recent_posts()
    posts = Post.objects.all()
    pinned = get_random_pinned_post()

    try:
        response = requests.get('https://www.boredapi.com/api/activity/')
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        quotes = response.json()
    except requests.exceptions.RequestException as e:
        # Handle the exception (e.g., log the error)
        print(f"An error occurred: {e}")
        quotes = []

    # Initialize the NewsApiClient with your API key
    newsapi = NewsApiClient(api_key=config('NEWS_API_KEY'))

    all_articles = newsapi.get_everything(q='destination OR adventure OR travel', language='en', sort_by='relevancy',
                                          page_size=3)

    # Extract the news articles from the response
    news_articles = []
    for article in all_articles['articles']:
        news_articles.append({
            'title': article['title'],
            'description': article['description'],
            'url': article['url']
        })

    context = {
        'posts': posts,
        'last_posts': last_posts,
        'pinned': pinned,
        'form': form,
        'quotes': quotes,
        'news_articles': news_articles
    }

    return render(request, 'coco/home.html', context)


def paginate_queryset(request, queryset, num_per_page=3):
    paginator = Paginator(queryset, num_per_page)
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results.
        paginated_queryset = paginator.page(paginator.num_pages)
    return paginated_queryset, page


def blog(request):
    queryset = Post.objects.filter(status='Published').order_by('-created_at')
    post_list, page = paginate_queryset(request, queryset)
    return render(request, 'coco/blog.html', {'page': page, 'post_list': post_list})


def dest_bulgaria(request):
    queryset = Post.objects.filter(status='Published', destination='Bulgaria').order_by('-created_at')
    post_list, page = paginate_queryset(request, queryset, num_per_page=2)
    return render(request, 'coco/coco-bulgaria.html', {'page': page, 'post_list': post_list})


def dest_abroad(request):
    queryset = Post.objects.filter(status='Published', destination='Abroad').order_by('-created_at')
    post_list, page = paginate_queryset(request, queryset, num_per_page=2)
    return render(request, 'coco/coco-abroad.html', {'page': page, 'post_list': post_list})


def dest_favourites(request):
    queryset = Post.objects.filter(status='Published', favourite=True).order_by('-created_at')
    post_list, page = paginate_queryset(request, queryset)
    return render(request, 'coco/coco-favourites.html', {'page': page, 'post_list': post_list})


def dest_where(request):
    places = PlacesVisited.objects.all()

    m = folium.Map(location=[49.44594350077738, 11.071861579494366], zoom_start=5)

    for place in places:
        coordinates = (place.latitude, place.longitude)
        popup_filled = f"<h3>{place.title}</h3><img src='{place.image.url}' " \
                       f"width=300px><p>{place.resume}</p><p>{place.date}</p>"
        if place.place_status == 'Loved':
            folium.Marker(coordinates,
                          popup=popup_filled,
                          tooltip=f'{place.tooltip}',
                          icon=folium.Icon(prefix='fa', icon='fa-heartbeat', color='red')).add_to(m)
        elif place.place_status == 'Home':
            folium.Marker(coordinates,
                          popup=popup_filled,
                          tooltip=f'{place.tooltip}',
                          icon=folium.Icon(icon='home', color='green')).add_to(m)
        elif place.place_status == 'Wanted':
            folium.Marker(coordinates,
                          popup='Wanted: '+popup_filled,
                          tooltip=f'{place.tooltip}',
                          icon=folium.Icon(prefix='fa', icon='fa-plane', color='purple')).add_to(m)

        else:
            folium.Marker(coordinates,
                          popup=popup_filled,
                          tooltip=f'{place.tooltip}',
                          icon=folium.features.CustomIcon(
                              'https://aleks-kostadinov.s3.eu-central-1.amazonaws.com/images/duck-blue.png',
                              icon_size=(28, 28))).add_to(m)

    context = {'map': m._repr_html_()}
    return render(request, 'coco/coco-where.html', context)


def about(request):
    return render(request, 'coco/about.html')


def contact(request):
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["title"]}'
            email_message = f'From: {form.cleaned_data["email"]}\n'
            email_message += f'Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n'
            email_message += f'Title: {form.cleaned_data["title"]}\n\n'
            email_message += form.cleaned_data['message']
            send_mail(
                email_subject,
                email_message,
                settings.CONTACT_EMAIL,
                [config('RECEPIENT_EMAIL')],
            )
            return render(request, 'coco/coco-success.html')
    form = MailMessageForm()
    context = {'form': form}
    return render(request, 'coco/coco-contact.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'coco/search.html', {'searched': searched, 'posts': posts})

    return render(request, 'coco/search.html')


def current_post(request, slug):
    post = get_object_or_404(Post, slug=slug, status='Published')
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'coco/post.html', {'post': post,
                                              'comments': comments,
                                              'new_comment': new_comment,
                                              'comment_form': comment_form})
