from . import views
from django.urls import path

urlpatterns = [
    path("count", views.increment_count),
    path("signup", views.sign_up, name="signup"),
    path("login", views.log_in),
    path("login-page", views.log_in_page),
]
