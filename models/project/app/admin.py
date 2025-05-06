from django.contrib import admin
# from .models import UserProfile
from .models import Student
from .models import Employee
from .models import Clients

# Register your models here.

# admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Clients)