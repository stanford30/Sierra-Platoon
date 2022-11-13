from django.urls import path
from . import views


urlpatterns = [path("pokemon/", views.index), path("pokemon2/", views.index)]
