from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='coco-home'),
    path('blog', views.blog, name='coco-blog'),
    path('post/<slug:slug>/', views.current_post, name='coco-post'),
    path('contact/', views.contact, name='coco-contact'),
    path('bulgaria', views.dest_bulgaria, name='coco-bulgaria'),
    path('abroad', views.dest_abroad, name='coco-abroad'),
    path('favourites', views.dest_favourites, name='coco-favourites'),
    path('where', views.dest_where, name='coco-where'),
    path('about', views.about, name='coco-about'),
    path('search', views.search, name='coco-search'),
    # path('confirm/<str:token>/', views.confirm_subscription, name='confirm_subscription'),
    # path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    # path('send-posts/', views.send_posts_to_subscribers, name='send_posts_to_subscribers'),

]
