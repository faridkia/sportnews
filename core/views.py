from django.shortcuts import render, HttpResponse, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('home:dashboard')
    else:
        return render(request, 'core/home.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'core/dashboard.html', context={'user':request.user})
    return redirect('home:home')