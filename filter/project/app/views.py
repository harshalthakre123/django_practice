from django.shortcuts import render

# Create your views here.

def home(request):
    data={ ,"name":"harshal", "age":21, "qualification":"b-tech"}
    return render(request, 'home.html', data)