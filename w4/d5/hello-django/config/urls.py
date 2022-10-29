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
    length = int(request.GET.get("length"))
    width = int(request.GET.get("width"))
    area = length * width
    return HttpResponse(area)


def rectanglePerimeter(request):
    length = int(request.GET.get("length"))
    width = int(request.GET.get("width"))
    p = 2 * (length + width)
    return HttpResponse(p)


def circleArea(request):

    radius = int(request.GET.get("radius"))
    area = math.pi * radius**2
    return HttpResponse(area)


def circlePerimeter(request):
    try:
        radius = int(request.GET.get("radius"))
    except:
        response = HttpResponse()
        response.status_code = 400
        return response
    circumference = 2 * math.pi * radius
    return HttpResponse(f"circumference: {circumference}")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("rectangle/area", rectangleArea),
    path("rectangle/perimeter", rectanglePerimeter),
    path("circle/area", circleArea),
    path("circle/perimeter", circlePerimeter),
]
