from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from core.models import *
from core.forms import CommentForm
from .forms import PostCreateForm
from django.contrib import messages

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/posts.html', context={'posts':posts})

def post_detail(request, id):
    spost = Post.objects.all()[1:5]
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
                                   'form': form, 'comments':comments, 'comment_count':comments.count(), 'spost':spost})
        else:
            redirect('accounts:login')
    else:
        form = CommentForm()
        return render(request, 'post/post_detail.html', context={'post':post, 'is_like':is_like, 'is_saved':is_saved,
                                                             'like_count':like_count, 'saved_count':saved_count,
                                                                 'form':form, 'comments':comments, 'comment_count':comments.count(),'spost':spost})




def post_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostCreateForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, 'پست با موفقیت ساخته شد')
                return redirect('home:dashboard')
        else:
            form = PostCreateForm()
        return render(request, 'post/post_create.html', context={'form': form})
    return redirect('accounts:login')

def post_delete(request, id):
    post = Post.objects.get(id=id)
    if post.author == request.user:
        post.delete()
        messages.success(request, 'پست با موفقیت پاک شد')
        return redirect('home:dashboard')
    else:
        messages.error(request, 'شما اجازه پاک کردن پست دیگران را ندارید.')
        return redirect('home:dashboard')

def post_edit(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        if post.author == request.user:
            if request.method == 'POST':
                form = PostCreateForm(request.POST, request.FILES, instance=post)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'پست با موفقیت ادیت شد')
                    return redirect('home:dashboard')
            else:
                form = PostCreateForm(instance=post)
            return render(request, 'post/post_edit.html', context={'form': form})
        else:
            messages.error(request, 'شما اجازه ادیت کردن پست دیگران را ندارید.')
            return redirect('home:dashboard')
    return redirect('accounts:login')