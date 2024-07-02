from django.urls import path
from src.user.views.register import Register
from src.user.views.login import Login

app_name = "user"

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
]
