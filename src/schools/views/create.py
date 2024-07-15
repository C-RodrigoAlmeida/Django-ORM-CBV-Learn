from django.views.generic import CreateView
from src.schools.models.school import School

class Create(CreateView):
    template_name = 'create.html'
    model = School