from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

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
    # print(request.method)
    # print(request.POST)
    # print(request.GET)
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
    image= request.POST.get('image')
    file= request.POST.get('file')
    password= request.POST.get('password')
    cpassword= request.POST.get('cpassword')
    user = Student.objects.filter(stu_email=email)
    if user:
        msg="User Already Exist"
        return render (request, 'reg.html', {'msg':msg})
    else :
        Student.objects.create(stu_email=email)
        msg="Registration Successful!"
        return render (request, 'login.html', {'msg':msg})
    # print(username, email, detail, phone, dob, subscribe, gender, password, cpassword)

    Student.objects.create(stu_name=username, stu_email=email, stu_dis=detail, stu_contact=phone, stu_dob=dob, stu_quali=subscribe, stu_gender=gender, stu_image=image, stu_file=file,stu_password=password)




def login(request):

    return render(request, "login.html")

