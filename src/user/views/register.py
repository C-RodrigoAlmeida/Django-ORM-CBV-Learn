from src.user.models.custom_user import CustomUser
from src.user.forms.register import RegisterForm
from django.views.generic import CreateView


class Register(CreateView):
    model = CustomUser
    form_class = RegisterForm
    success_url = "/login/"
    template_name = "register.html"
