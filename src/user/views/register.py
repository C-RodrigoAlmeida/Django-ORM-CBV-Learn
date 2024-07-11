from src.user.models.custom_user import CustomUser
from src.user.forms.register import RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class Register(CreateView):
    model = CustomUser
    form_class = RegisterForm
    success_url = reverse_lazy('user:login')
    template_name = "register.html"
