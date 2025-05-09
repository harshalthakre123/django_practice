from django.contrib import admin
from .models import Aadhar, User, Department, Student, Vehicle, Fuel
# Register your models here.

admin.site.register(User)
admin.site.register(Aadhar)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Vehicle)
admin.site.register(Fuel)