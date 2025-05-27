from django import forms
from .models import Post, UploadedFile, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'image']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

