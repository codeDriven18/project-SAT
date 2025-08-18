# accounts/admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "role", "full_name")
    list_filter = ("role",)
    search_fields = ("username", "full_name")
