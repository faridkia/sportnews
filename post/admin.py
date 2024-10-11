from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'created_at']
    search_fields = ['author', 'title']
    list_filter = ['created_at']
