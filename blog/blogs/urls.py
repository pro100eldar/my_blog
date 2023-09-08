from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]