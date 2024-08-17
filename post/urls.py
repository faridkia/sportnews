from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path('posts', views.post_list, name='posts'),
]