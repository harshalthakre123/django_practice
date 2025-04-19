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
    
    print(username, email, detail, phone, dob, subscribe, gender, password, cpassword, file, image)
   

    
    user = Student.objects.filter(stu_email=email)
    if user:
        msg="User Already Exist"
        return render (request, 'reg.html', {'msg':msg})
    else :
        if password==cpassword:
            Student.objects.create(stu_name=username, stu_email=email, stu_dis=detail, stu_contact=phone, stu_dob=dob, stu_quali=subscribe, stu_gender=gender, stu_image=image, stu_file=file,stu_password=password)
            msg="Registration Successful!"
            return render(request, 'login.html', {'msg':msg})
        else:
            msg="Password and Confirm Password not matched"
            userdata={
                "username":username,
                "email":email,
                "detail":detail,
                "phone":phone,
                "dob": dob,
                "subscribe": subscribe,
                "gender": gender,
                "image": image,
                "file" :file,
            }
            return render(request, 'reg.html', {'msg':msg , "data":userdata})



    

    



def login(request):
#     if request.method=="POST":
#         email=request.POST.get("e.mail")
#         password=request.POST.get("password")
    return render(request, "login.html")

def logindata(request):
    if request.method == "POST":
        e= request.POST.get('email')
        p= request.POST.get('password')
        user=Student.objects.filter(stu_email=e)
        if user:
            userdata=Student.objects.get(stu_email=e)
            print(userdata.stu_name)
            print(userdata.stu_email)
            p1=userdata.stu_password
            if p==p1:
                info={"id":userdata.id , "email":userdata.stu_email, "name":userdata.stu_name, "dob":userdata.stu_dob, "qualification":userdata.stu_quali , "phone":userdata.stu_contact, "password":userdata.stu_password, "file":userdata.stu_image}
                return render(request, 'dashboard.html', {"info":info, 'userdata':userdata})
                
                
            else:
                pmsg="password not Matched"
                return render(request, 'login.html', {"pmsg":pmsg, "email":e})
        else:
            msg="email not Exist"
            return render(request, 'login.html', {"msg":msg})
    else:
        return render(request, 'login.html')
    

