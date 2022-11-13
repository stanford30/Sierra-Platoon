from django.shortcuts import render

# Create your views here.
def brands(request):
    from django.http import HttpResponse

    return HttpResponse("hello World")
