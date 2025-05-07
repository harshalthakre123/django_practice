from django.shortcuts import render
from .models import User, Aadhar, Department, Student

# Create your views here.


# One to One

def user(request):
    data=User.objects.all()
    print(data)
    print()
    print(data.values())
    print()
    print(data.values_list())

    data1=User.objects.get(name='Harshal')
    print(data1.name)
    print(data1.email)
    print(data1.contact)
    # print(data1.aadhar)
    print(data1.aadhar_no.aadhar)
    print(data1.aadhar_no.created_by)

def aadhar(request):
    data=Aadhar.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    data2=Aadhar.objects.get(aadhar='12345')
    print(data2.user_info.name)
    print(data2.user_info.email)
    print(data2.user_info.contact)
    # print(data2.aadhar)
    print(data2.user_info.aadhar_no.aadhar)
    print(data2.user_info.aadhar_no.created_by)


#one to many

def student(request):
    data=Student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    # # Forward data access(from stu to depart)
    stu_data= Student.objects.get(stu_name="Nikhil Patel")
    print(stu_data.id)
    print(stu_data.stu_name)
    print(stu_data.stu_email)

    # x=stu_data.stu_dep

    # print(x.dep_name)
    # print(x.dep_des)
    # print(x.dep_hod)

    # print(stu_data.stu_dep.dep_name)
    # print(stu_data.stu_dep.dep_des)
    # print(stu_data.stu_dep.dep_hod)

# def department(request):
#     data=Department.objects.all()
#     print(data)
#     print(data.values())
#     print(data.values_list())

#     # Forward data access(from stu to depart)
#     stu_data= Department.objects.get(id=1)
#     print(dep_data.id)
#     print(dep_data.dep_name)
#     print(dep_data.dep_des)
#     print(dep_data.dep_hod)

#     print((dep_data.depart.all()).count())

#     x=dep_data.depart.all()



