from django.db import models
from src.core.models.base_model import BaseModel
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class CustomUser(BaseModel, AbstractUser):
    role = models.ForeignKey("Role", on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="customuser_set",
        related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="customuser_set",
        related_query_name="customuser",
    )

    def __str__(self):
        return self.name
