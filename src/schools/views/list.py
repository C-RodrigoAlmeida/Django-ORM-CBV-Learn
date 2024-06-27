from django.views.generic import ListView
from src.schools.models.schools import Schools


class SchoolsListView(ListView):
    context_object_name = "schools"
    model = Schools
    template_name = "list.html"
