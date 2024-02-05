from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from account.models import User
from .forms import PostForm
from django.contrib import messages


# Create your views here.


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('posts:create')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def posts(request):
    posts_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list': posts_list
    }
    return render(request, 'posts/detail-posts.html', context)


def post(request, id):
    context = {
        'post': get_object_or_404(Post, id=id)
    }
    selected=Post.objects.filter(id=context['post'].id)
    if selected.exists():
        context['selected'] = selected.get()
        return render(request, 'posts/detail-post.html', context)
