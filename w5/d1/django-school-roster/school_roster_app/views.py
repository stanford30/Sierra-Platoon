from django.shortcuts import render

# Create your views here.
from .models import School  # import our School class

my_school = School("Django School")  # create a school instance


def index(request):
    my_data = {"school_name": my_school.name}
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    all_staff = my_school.staff
    context = {"all_staff": all_staff}
    return render(request, "pages/staff.html", context)


def staff_detail(request, employee_id):
    staff = my_school.find_staff_by_id(employee_id)

    return render(request, "pages/staff-detail.html", {"staff": staff.__dict__})


def list_students(request):
    all_students = my_school.students
    context = {"all_students": all_students}
    return render(request, "pages/students.html", context)


def student_detail(request, school_id):
    student = my_school.find_student_by_id(school_id)

    return render(request, "pages/student-detail.html", {"student": student.__dict__})
