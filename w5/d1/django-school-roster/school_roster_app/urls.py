from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("staff/", views.list_staff, name="list_staff"),
    path("staff/<int:employee_id>", views.staff_detail, name="staff_detail"),
    path("students/", views.list_students, name="list_students"),
]
