from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='posts'),
    path('<int:id>', views.post_detail, name='post_detail'),
]