from django.db import models

# quail = [(1,’B.Tech’),(2,”M.Tech”)]
# class UserProfile(models.Model):
#     quail = [("1",'B.Tech'),("2",'M.Tech')] 
#     username= models.CharField(max_length=30, null=True, unique=True, db_index=True, blank=False, help_text="Enter a unique username")
#     email= models.EmailField(max_length=255, unique=True, blank=False, db_index=True)
#     bio= models.CharField(max_length=50, blank=True, null=True, db_index=True,help_text="Write a short bio about yourself")
#     is_active= models.BooleanField(default=False,db_index=True)
#     Qualification=models.CharField(max_length=100, choices=quail ,null=True,verbose_name= 'Quali',db_index=True)

#     def __str__(self):
#                 return self.email


class BaseInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255, unique=True, blank=False, db_index=True)
    contact=models.IntegerField(max_length=10)
    
    class Meta:
        abstract=True

class Student(BaseInfo):
    branch=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Employee(BaseInfo):
    department=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    def __str__(self):
        return self.name            
class Clients(BaseInfo):
    project=models.CharField(max_length=255)
    def __str__(self):
        return self.name