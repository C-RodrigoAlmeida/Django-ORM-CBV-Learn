from django.db import models
from src.core.models.base_model import BaseModel
from src.schools.models.school import School
from src.user.models.custom_user import CustomUser

class SchoolTenant(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="school_tenant")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="school_tenant")
    graduation = models.ForeignKey(School, on_delete=models.CASCADE, related_name="school_tenant_graduation")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'school'], name='unique_user_school'),
            models.CheckConstraint(
                check=models.Q(school__isnull=False) 
                & models.Q(user__isnull=False)
                & models.Q(graduation__isnull=False),
                name='no_empty_fields'
            )
        ]