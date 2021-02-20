from django.urls import path

from . import views

app_name = "meet_someone"

urlpatterns = [
    path("", views.index, name="index")
]
