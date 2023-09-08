from django.contrib import admin

from .models import BlogPost, Post

admin.site.register(BlogPost)
admin.site.register(Post)