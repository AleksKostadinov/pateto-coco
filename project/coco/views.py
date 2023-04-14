from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'coco/home.html', {'posts': posts})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'coco/blog.html', {'posts': posts})


def dest_bulgaria(request):
    posts = Post.objects.all()
    return render(request, 'coco/coco-bulgaria.html', {'posts': posts})


def dest_abroad(request):
    posts = Post.objects.all()
    return render(request, 'coco/coco-abroad.html', {'posts': posts})


def dest_where(request):
    return render(request, 'coco/coco-where.html')


def about(request):
    return render(request, 'coco/about.html')
