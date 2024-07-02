from django import forms
from src.user.models.custom_user import CustomUser
from src.user.models.role import Role


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "role"]

    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, kwargs)
        self.fields["password"].widget = forms.PasswordInput()
