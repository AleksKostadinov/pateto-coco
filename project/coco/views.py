from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from random import choice


def get_recent_posts():
    return Post.objects.filter(status='Published')[:6]


def get_random_pinned_post():
    pinned_posts = Post.objects.filter(pinned=True, status='Published')
    return choice(pinned_posts) if pinned_posts else None


def home(request):
    last_posts = get_recent_posts()
    posts = Post.objects.all()
    pinned = get_random_pinned_post()
    return render(request, 'coco/home.html', {'posts': posts, 'last_posts': last_posts, 'pinned': pinned})


def current_post(request, slug):
    post = get_object_or_404(Post, slug=slug, status='Published')

    context = {
        'post': post,
    }
    return render(request, 'coco/post.html', context)


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


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'coco/search.html', {'searched': searched, 'posts': posts})

    return render(request, 'coco/search.html')
