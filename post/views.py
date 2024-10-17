from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from core.models import *
from core.forms import CommentForm
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/posts.html', context={'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(is_ok=True).all()
    if request.user.is_authenticated:
        if request.user.likes.filter(post=post).exists():
            is_like = True
        else:
            is_like = False
        if request.user.saved.filter(post=post).exists():
            is_saved = True
        else:
            is_saved = False
    else:
        is_like = False
        is_saved = False
    like_count = Like.objects.filter(post=post).count()
    saved_count = Saved.objects.filter(post=post).count()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                Comment.objects.create(user=request.user, post=post, text=form.cleaned_data['text'])
                return redirect('post:post_detail', id=post.id)
            return render(request, 'post/post_detail.html',
                          context={'post': post, 'is_like': is_like, 'is_saved': is_saved,
                                   'like_count': like_count, 'saved_count': saved_count,
                                   'form': form, 'comments':comments, 'comment_count':comments.count()})
        else:
            redirect('accounts:login')
    else:
        form = CommentForm()
        return render(request, 'post/post_detail.html', context={'post':post, 'is_like':is_like, 'is_saved':is_saved,
                                                             'like_count':like_count, 'saved_count':saved_count,
                                                                 'form':form, 'comments':comments, 'comment_count':comments.count()})

