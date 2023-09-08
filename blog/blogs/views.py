from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost, Post
from .forms import BlogForm, PostForm


def index(request):
    return render(request, 'blogs/index.html')

def blogs(request):
    blogs = BlogPost.objects.order_by('title')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    posts = blog.post_set.order_by('date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog_post = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    blog = post.blog_post
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'blog': blog, 'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)


