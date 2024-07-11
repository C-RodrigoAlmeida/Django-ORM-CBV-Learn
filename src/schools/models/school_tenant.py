from django.db import models
from src.core.models.base_model import BaseModel
from src.schools.models.school import School
from src.user.models.custom_user import CustomUser

class SchoolTenant(BaseModel):
    models.ForeignKey(School, on_delete=models.CASCADE)
    models.ForeignKey(CustomUser, on_delete=models.CASCADE)