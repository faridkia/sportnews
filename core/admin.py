from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']

@admin.register(Saved)
class SavedAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']