from django.contrib import admin
from .models import Post, UploadedFile, Comment

# Enhanced display for comments in admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'created_at')
    search_fields = ('text', 'author__username', 'post__title')
    list_filter = ('created_at', 'author')

# Register other models as usual
admin.site.register(Post)
admin.site.register(UploadedFile)

