from django.shortcuts import render, HttpResponse

def gholam(request):
    return render(request, 'core/home.html')
