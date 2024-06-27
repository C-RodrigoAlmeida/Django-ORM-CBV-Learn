from django.urls import path
from src.schools.views.details import SchoolsDetailsView
from src.schools.views.list import SchoolsListView

app_name = "schools"

urlpatterns = [
    path("", SchoolsListView.as_view(), name="list"),
    path("<uuid:id>/", SchoolsDetailsView.as_view(), name="details"),
]
