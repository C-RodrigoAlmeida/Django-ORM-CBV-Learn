from django import forms
from django.contrib.auth.forms import UserCreationForm
from src.user.models.custom_user import CustomUser
from src.user.models.role import Role


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "role"]

    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput()
        self.fields["password2"].widget = forms.PasswordInput()
