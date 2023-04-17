from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    STATUS = (
        (0, 'Draft'),
        (1, 'Published')
    )

    DESTINATION = (
        (0, 'Bulgaria'),
        (1, 'Abroad')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    resume = models.TextField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    favourite = models.BooleanField(default=False)
    destination = models.IntegerField(choices=DESTINATION, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

