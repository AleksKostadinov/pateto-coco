from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'created_at', 'favourite', 'destination')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    # date_hierarchy = 'created_at'
    ordering = ['status', '-created_at']


admin.site.register(Post, PostAdmin)
