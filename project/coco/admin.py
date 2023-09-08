from django.contrib import admin
from .models import Post, Comment, Subscribers, MailMessage, PlacesVisited


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'created_at', 'favourite', 'destination', 'pinned')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'created_at'
    ordering = ['status', '-created_at']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    list_filter = ('date',)
    search_fields = ('email',)


admin.site.register(Subscribers, SubscribersAdmin)


class MailMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'title', 'date')
    list_filter = ('date',)
    search_fields = ('email', 'title')


admin.site.register(MailMessage, MailMessageAdmin)


class PlacesVisitedAdmin(admin.ModelAdmin):
    list_display = ('places', 'latitude', 'longitude', 'date')
    list_filter = ('places', 'date')
    search_fields = ('places',)


admin.site.register(PlacesVisited, PlacesVisitedAdmin)
