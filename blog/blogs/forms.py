from django import forms

from .models import BlogPost, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']
        labels = {'title': ''}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text': 'Post:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
