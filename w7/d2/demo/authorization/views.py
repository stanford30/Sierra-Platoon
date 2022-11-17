from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .models import AppUser as User
import json


@csrf_exempt
def sign_up(request):
    try:
        body = json.loads(request.body)
        User.objects.create_user(
            username=body["username"], password=body["password"], email=body["username"]
        )
    except Exception as e:
        print("oops")
        print(str(e))
    return HttpResponse("hi")
