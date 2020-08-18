from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def user(request):
    return HttpResponse("hello , user no greet")
#def greet(request,name):
#    return HttpResponse(f"hello , {name.capitalize()} ")
def greets(request,name):
    return render(request , "hello/greets.html", {
        "name": name.capitalize()
    })
