from django.urls import path
from src.user.views.login import user_login, user_logout, user_resgistration

app_name = 'user'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_resgistration, name='registration'),
]