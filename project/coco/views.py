from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_recent_posts():
    return Post.objects.filter(status='Published')[:4]


def home(request):
    last_posts = get_recent_posts()
    posts = Post.objects.all()
    return render(request, 'coco/home.html', {'posts': posts, 'last_posts': last_posts})


def blog(request):
    object_list = Post.objects.filter(status='Published').order_by('-created_at')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'coco/blog.html',
                  {'page': page,
                   'post_list': post_list})


def current_post(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
    }
    return render(request, 'coco/post.html', context)


def dest_bulgaria(request):
    object_list = Post.objects.filter(status='Published', destination='Bulgaria').order_by('-created_at')
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'coco/coco-bulgaria.html',
                  {'page': page,
                   'post_list': post_list})


def dest_abroad(request):
    object_list = Post.objects.filter(status='Published', destination='Abroad').order_by('-created_at')
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'coco/coco-abroad.html',
                  {'page': page,
                   'post_list': post_list})


def dest_favourites(request):
    object_list = Post.objects.filter(status='Published', favourite=True).order_by('-created_at')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'coco/coco-favourites.html',
                  {'page': page,
                   'post_list': post_list})


def coco_places(request):
    object_list = Post.objects.filter(status='Published', favourite=True).order_by('-created_at')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'coco/coco-places.html',
                  {'page': page,
                   'post_list': post_list})

def dest_where(request):
    return render(request, 'coco/coco-where.html')


def about(request):
    return render(request, 'coco/about.html')
