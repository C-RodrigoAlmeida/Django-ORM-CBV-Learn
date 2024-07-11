from django.views.generic import DetailView
from src.schools.models.school import School


class SchoolsDetailsView(DetailView):
    context_object_name = "school_detail"
    model = School
    template_name = "details.html"
