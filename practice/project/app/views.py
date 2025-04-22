from django.shortcuts import render
from django.http import HttpsResponse
from models import Users

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
    # print("METHOD:-")
    # print(request.method)
    # print("POST:-")
    # print(request.POST)
    # print("FILES:-")
    # print(request.FILES)
    # print("GET:-")
    # print(request.GET)
    # print('COOKIES:-')
    # print(request.COOKIES)
    # print("META:-")
    # print(request.META)

    username=request.POST.get('username')
    email=request.POST.get('email')
    age=request.POST.get('age')
    dob=request.POST.get('dob')
    gender=request.POST.get('gender')
    phone=request.POST.get('phone')
    qualification=request.POST.getlist('qualifications')
    remarks=request.POST.get('remarks')
    profile=request.FILES.get('profile_img')
    aadhar=request.FILES.get('aadhar')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    print(username, ",", email, ",", age, ",", dob, ",", gender, ",", phone, ",", qualification, ",", remarks, ",", profile, ",", aadhar, ",", password, ",", cpassword)

    user= Users.object.filter(user_email=email)

    if user:
        msg="User Already Registered!"
        return render(request, 'register.html', {"msg": msg})
    else:
        if password==cpassword:
            Users.objects.create(user_name=username, user_email=email, user_age=age, user_dob=dob, user_gender=gender, user_phone=phone, user_quali=qualification, user_remarks=remarks, user_profile=profile, user_aadhar=aadhar, user_password=password)
            msg="registered Successfully!"
            return render(request,'login.html', {"msg": msg})
        else:
            msg="Password and confirm password not matched."
            userdata={"username":username,
                      "email": email,
                      "age":age,
                      "dob":dob,
                      "gender":gender,
                      "phone":phone,
                      "qualification":qualification,
                      "remarks":remarks,
                      "profile": profile,
                      "aadhar":aadhar,
                      "password":password}
            return render(request, "register.html", {"data":userdata})


def logindata(request):
    if request.method == "POST":
        e=request.POST.get("email")
        p=request.POST.get("password")
         
    return render(request, "userdash.html", {"msg":msg})

# def dashboard(request):
#     return render(request, "userdash.html")