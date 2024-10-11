from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/posts.html', context={'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/post_detail.html', context={'post':post})

