from django.contrib import admin
from django.urls import path

from .views import create_post, posts, post

app_name = 'posts'

urlpatterns = [
    path('create_posts/', create_post, name='create'),
    path('list_posts/', posts, name='list'),
    path('post/<int:id>', post, name='post')
]
