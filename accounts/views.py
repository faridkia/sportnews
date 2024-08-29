from django.shortcuts import render, HttpResponse
from .forms import SignUpForm
import sqlite3
from .models import User
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], password=cd['password'])
            return HttpResponse('User Sakhte Shod')
        else:
            return render(request, 'accounts/signup.html', context={'form':form})
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', context={'form':form})

def insert(request):
    form = SignUpForm(request.POST)

    query = "insert into table users(username, password) values ()"