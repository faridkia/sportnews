from django.shortcuts import render, HttpResponse
from .forms import SignUpForm

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        return HttpResponse(f'Salam')
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', context={'form':form})