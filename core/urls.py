from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('like/<int:id>', views.like_post, name='like'),
    path('saved/<int:id>', views.saved_post, name='saved'),
]