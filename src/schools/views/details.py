from django.views.generic import DetailView
from src.schools.models.schools import Schools


class SchoolsDetailsView(DetailView):
    context_object_name = "school_detail"
    model = Schools
    template_name = "details.html"
