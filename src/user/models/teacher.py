from django.db import models

from core.models.base_model import BaseModel


class Teacher(models.Model, BaseModel):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    last_name = models.CharField(max_length=100)
    teaching_areas_id = models.ForeignKey()
