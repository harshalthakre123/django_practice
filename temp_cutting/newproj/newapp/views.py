from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello")
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def reg(request):
    return render(request, "reg.html")

def registerdata(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    print(request.FILES)
    print(request.COOKIES)
    print(request.META)
    print(request.SETTINGS)
def login(request):
    return render(request, "login.html")

