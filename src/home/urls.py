from django.urls import path
from src.home.views.about import About
from src.home.views.index import Index

app_name = "home"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("about/", About.as_view(), name="about"),
]
