from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from random import choice
from .forms import CommentForm, SubscribersForm


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
    return render(request, 'coco/home.html', {'posts': posts, 'last_posts': last_posts, 'pinned': pinned, 'form': form})


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
    return render(request, 'coco/coco-where.html')


def about(request):
    return render(request, 'coco/about.html')


def contact(request):
    return render(request, 'coco/coco-contact.html')


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
