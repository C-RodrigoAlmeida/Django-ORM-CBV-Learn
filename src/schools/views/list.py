from django.views.generic import ListView
from src.schools.models.school import School


class SchoolsListView(ListView):
    context_object_name = "schools"
    model = School
    template_name = "list.html"
