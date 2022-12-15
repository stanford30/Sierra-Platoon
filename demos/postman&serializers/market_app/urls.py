from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.categories),
    path("items/", views.items),
    path("categories/<int:id>/", views.category_detail),
    path("items/<int:id>/", views.item_detail),
]
