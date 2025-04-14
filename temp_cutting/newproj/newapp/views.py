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
    # print(request.FILES)
    # print(request.COOKIES)
    # print(request.META)
    # print(request.SETTINGS)
    username= request.POST.get('username')
    email= request.POST.get('email')
    detail= request.POST.get('detail')
    phone= request.POST.get('phone')
    dob= request.POST.get('dob')
    subscribe= request.POST.getlist('subscribe')
    gender= request.POST.get('gender')
    password= request.POST.get('password')
    cpassword= request.POST.get('cpassword')
    print(username, email, detail, phone, dob, subscribe, gender, password, cpassword)


def login(request):
    return render(request, "login.html")

