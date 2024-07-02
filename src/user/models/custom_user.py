from django.db import models
from core.models.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(BaseModel, AbstractUser):
    role = models.ForeignKey("Role", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
