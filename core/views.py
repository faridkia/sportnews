from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from post.models import Post
def home(request):
    if request.user.is_authenticated:
        return redirect('home:dashboard')
    else:
        return render(request, 'core/home.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()[:8]
        return render(request, 'core/dashboard.html', context={'user':request.user, 'posts':posts})
    return redirect('home:home')

def like_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        if Like.objects.filter(user=request.user, post=post).exists():
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return redirect('post:post_detail', id=id)
        else:
            Like.objects.create(user=request.user, post=post)
            return redirect('post:post_detail', id=id)
    else:
        return redirect('accounts:login')


def saved_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        if Saved.objects.filter(user=request.user, post=post).exists():
            saved = Saved.objects.get(user=request.user, post=post)
            saved.delete()
            return redirect('post:post_detail', id=id)
        else:
            Saved.objects.create(user=request.user, post=post)
            return redirect('post:post_detail', id=id)
    else:
        return redirect('accounts:login')
