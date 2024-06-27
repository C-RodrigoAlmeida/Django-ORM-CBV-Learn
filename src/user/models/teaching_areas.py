from django.db import models
from core.models.base_model import BaseModel


class TeachingAreas(models.Model, BaseModel):
    name = models.CharField(max_length=255)
