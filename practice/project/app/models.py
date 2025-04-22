from django.db import models

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_age = models.IntegerField()
    user_dob = models.DateField()
    user_gender = models.CharField(max_length=50)
    user_phone = models.IntegerField()
    user_quali = models.CharField(max_length=50)
    user_remarks = models.CharField(max_length=200)
    user_profile = models.ImageField(upload_to='image/')
    user_file = models.FileField(upload_to='file/')
    user_password = models.CharField(max_length=15)