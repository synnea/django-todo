from django.shortcuts import render, HttpResponse

def say_hello(request):
    return HttpResponse("Hello World!")

# Create your views here.
