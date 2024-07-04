from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)