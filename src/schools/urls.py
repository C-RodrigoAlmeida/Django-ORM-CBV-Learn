from django.urls import path
from src.schools.views.details import SchoolsDetailsView
from src.schools.views.list import SchoolsListView
from src.schools.views.create import SchoolsCreateView

app_name = "schools"

urlpatterns = [
    path("", SchoolsListView.as_view(), name="list"),
    path('create/', SchoolsCreateView.as_view(), name="create"),
    path("<uuid:id>/", SchoolsDetailsView.as_view(), name="details"),
]
