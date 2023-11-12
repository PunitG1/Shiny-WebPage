from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#view function takes a request and gives response
#AKA request handler

def say_hello(request):
    return HttpResponse("Hello world")

