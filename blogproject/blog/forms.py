from django import forms
from .models import Post, UploadedFile, Comment
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'file']

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Comment
        fields = ['text']
