from django.views.generic import CreateView
from src.schools.models.school import School
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class SchoolsCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'create.html'
    model = School