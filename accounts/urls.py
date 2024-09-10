from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.SignUp, name='signup'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout')
]