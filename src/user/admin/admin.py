# src/user/admin.py
from django.contrib import admin
from src.user.models.custom_user import CustomUser
from src.user.models.role import Role


admin.site.register(CustomUser)
admin.site.register(Role)