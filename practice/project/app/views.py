from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


def registerdata(request):
    print(request.method)

def logindata(request):
    msg="Login Successfully!"
    return render(request, "userdash.html", {"msg":msg})

# def dashboard(request):
#     return render(request, "userdash.html")