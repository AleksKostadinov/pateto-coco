from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='coco-home'),
    path('blog', views.blog, name='coco-blog'),
    path('post/<slug:slug>/', views.current_post, name='coco-post'),
    path('bulgaria', views.dest_bulgaria, name='coco-bulgaria'),
    path('abroad', views.dest_abroad, name='coco-abroad'),
    path('where', views.dest_where, name='coco-where'),
    path('about', views.about, name='coco-about'),
]
