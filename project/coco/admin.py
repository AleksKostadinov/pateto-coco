from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'published_on')
    list_filter = ('status', 'published_on', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    # date_hierarchy = 'published_on'
    ordering = ['status', '-published_on']


admin.site.register(Post, PostAdmin)
