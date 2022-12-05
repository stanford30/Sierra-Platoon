from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Item, Category
from rest_framework.decorators import api_view
from .serializers import CategorySerializer, ItemSerializer


# Create your views here.


# def send_the_homepage(request):
#     print("home")
#     theIndex = open("static/index.html").read()
#     return HttpResponse(theIndex)


@api_view(["GET"])
def categories(request):
    if request.method == "GET":
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        # print(serializer.get_field_names)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def items(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
