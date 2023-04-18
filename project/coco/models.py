from django.contrib.auth.models import User
from django.db import models


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
    content = models.TextField()
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

