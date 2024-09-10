from django.shortcuts import render, HttpResponse, redirect
from .forms import *
import sqlite3
from .models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import
def SignUp(request):
    if request.user.is_authenticated:
        return redirect('home:dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], password=cd['password'])
            return redirect('home:dashboard')
        else:
            return render(request, 'accounts/signup.html', context={'form':form})
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', context={'form':form})

def Login(request):
    if request.user.is_authenticated:
        return redirect('home:dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:dashboard')
            else:
                form.add_error('username', 'The Username/password is incorrect')
                return render(request, 'accounts/login.html', context={'form':form})
        else:
            return render(request, 'accounts/login.html', context={'form':form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', context={'form':form})

def Logout(request):
    logout(request)
    return redirect('home:home')