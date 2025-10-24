from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("patata", views.patata, name="patata"),
]
