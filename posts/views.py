from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from account.models import User
from .forms import PostForm


# Create your views here.


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('posts:create')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
