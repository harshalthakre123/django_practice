from django.shortcuts import render
from .models import User, Aadhar

# Create your views here.


def Student(request):
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