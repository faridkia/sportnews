from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username']
    fieldsets = UserAdmin.fieldsets + (
        ('More info',
         {'fields':
              ('image',)}),
    )
    search_fields = ['username']
