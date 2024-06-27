from django.db import models
from src.core.models.base_model import BaseModel


# Create your models here.
class Schools(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
