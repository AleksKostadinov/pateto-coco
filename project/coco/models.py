from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )

    DESTINATION = (
        ('Bulgaria', 'Bulgaria'),
        ('Abroad', 'Abroad')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    resume = models.TextField(max_length=500)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS, default='Draft')
    favourite = models.BooleanField(default=False)
    destination = models.TextField(choices=DESTINATION, default='Bulgaria')
    pinned = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.name} on {self.created_on}'


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class PlacesVisited(models.Model):
    places = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Places Visited"

    def __str__(self):
        return self.places
