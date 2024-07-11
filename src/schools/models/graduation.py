from django.db import models
from src.core.models.base_model import BaseModel

class Graduation(BaseModel):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name