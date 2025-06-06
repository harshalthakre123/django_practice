from django.db import models

# Create your models here.


# one to one

class Aadhar(models.Model):
    aadhar=models.IntegerField(unique=True)
    created_by=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.aadhar)

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.IntegerField()
    aadhar_no=models.OneToOneField(Aadhar, on_delete=models.PROTECT, to_field="aadhar", related_name="user_info")

    def __str__(self):
        return self.name


# one to many

class Department(models.Model):
    dep_name= models.CharField(max_length=50, unique=True)
    dep_des= models.TextField(max_length=200)
    dep_hod=models.CharField(max_length=50)

class Student(models.Model):
    stu_name= models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_dep=models.ForeignKey(Department, on_delete=models.PROTECT, to_field='dep_name', related_name="depart")
    def __str__(self):
        return self.stu_name
    


# many to many

class Fuel(models.Model):
    fuel_name=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.fuel_name

class Vehicle(models.Model):
    vehicle_name=models.CharField(max_length=50)
    fuel_type=models.ManyToManyField(Fuel, related_name="Vehicle")
    def __str__(self):
        return self.vehicle_name
    

class Ht(models.Model):
    name=models.CharField(max_length=50)