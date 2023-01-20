from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
  return render(request, "hello/index.html")

def carlos(request) :
  return HttpResponse("Hello, Carlos!!!")

def mike(request) :
  return HttpResponse("Hello, Mike!!!!!")

def greet(request, name) :
  return render(request, "hello/greet.html", {
    "name": name.capitalize()
  })

def index(request):
  return HttpResponse("<h1 style=\"color:blue\">Hello, World!</h1>")
