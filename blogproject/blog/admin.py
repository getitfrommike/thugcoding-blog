from django.contrib import admin
from django import forms
from .models import Post, UploadedFile, Comment
from django_ckeditor_5.widgets import CKEditor5Widget


# Admin form for Post model
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Post
        fields = '__all__'

    class Media:
        css = {
            'all': ('blog/admin.css',),  # Points to static/blog/admin.css
        }


# Admin form for Comment model
class CommentAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Comment
        fields = '__all__'

    class Media:
        css = {
            'all': ('blog/admin.css',),  # Points to static/blog/admin.css
        }


# Admin class for Post
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')


# Admin class for Comment
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ('post', 'author', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('author__username', 'text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# Register all models with admin
admin.site.register(Post, PostAdmin)
admin.site.register(UploadedFile)
admin.site.register(Comment, CommentAdmin)
