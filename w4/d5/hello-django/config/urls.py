"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math


def rectangleArea(request):
    # print(dir(request))
    # print(request.META["QUERY_STRING"])
    # print(request.GET.get("name"))
    try:
        length = int(request.GET.get("length"))
        width = int(request.GET.get("width"))
    except:
        return badResponse()

    area = length * width
    return HttpResponse(area)


def rectanglePerimeter(request):
    try:
        length = int(request.GET.get("length"))
        width = int(request.GET.get("width"))
    except:
        response = HttpResponse()
        response.status_code = 400
        return response

    p = 2 * (length + width)
    return HttpResponse(p)


def circleArea(request):
    try:
        radius = int(request.GET.get("radius"))
    except:
        return badResponse()

    area = math.pi * radius**2
    response = HttpResponse(f"area = {area}")
    response.status_code = 200
    return response


def circlePerimeter(request):
    try:
        radius = int(request.GET.get("radius"))
    except:
        response = HttpResponse()
        response.status_code = 400
        return response
    circumference = 2 * math.pi * radius
    return HttpResponse(f"circumference: {circumference}")


def badResponse():
    response = HttpResponse()
    response.status_code = 400
    return response


def rectangleAreaWithParams(request, height, width):
    area = height * width
    response = HttpResponse(f"area={area}")
    response.status_code = 200
    return response


def rectanglePerimeterWithParams(request, height, width):
    perimeter = 2 * (height + width)
    response = HttpResponse(f"perimeter={perimeter}")
    response.status_code = 200
    return response


def circleAreaWithParams(request, radius):
    area = radius**2 * math.pi
    response = HttpResponse(f"area={area}")
    response.status_code = 200
    return response


"""
/rectangle/perimeter/<int:height>/<int:width>
/circle/area/<int:radius>
/circle/perimeter/<int:radius>
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path("rectangle/area", rectangleArea),
    path("rectangle/perimeter", rectanglePerimeter),
    path("circle/area", circleArea),
    path("circle/perimeter", circlePerimeter),
    path("rectangle/area/<int:height>/<int:width>", rectangleAreaWithParams),
    path("rectangle/perimeter/<int:height>/<int:width>", rectanglePerimeterWithParams),
    path("circle/area/<int:radius>", circleAreaWithParams),
]
