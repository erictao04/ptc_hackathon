from django.urls import path

from . import views

app_name = "my_groups"

urlpatterns = [
    path("", views.index, name="index")
]
