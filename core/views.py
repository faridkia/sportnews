from django.shortcuts import render, HttpResponse

def home(request):
    if request.user.is_authenticated:
        return render(request, 'core/home.html', context={'user':request.user})
    else:
        return render(request, 'core/home.html', context={'user':''})
