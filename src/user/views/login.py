from src.user.forms.login import loginForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login


class loginView(TemplateView):
    template_name = "login.html"
    form_class = loginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            if user is not None:
                login(request, user)
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)
