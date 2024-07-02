from django.contrib import admin
from src.user.models.custom_user import CustomUser
from src.user.models.custom_user import Role

admin.site.register(CustomUser)
admin.site.register(Role)
