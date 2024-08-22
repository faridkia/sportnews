from django.db import models
from django.contrib.auth.models import AbstractUser

def user_image_upload_path(instance, filename):
    return f"users/{instance.username}/{filename}"

class User(AbstractUser):
    image = models.ImageField(upload_to=user_image_upload_path, verbose_name='عکس')
