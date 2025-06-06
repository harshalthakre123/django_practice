# Generated by Django 5.2 on 2025-04-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stu_name", models.CharField(max_length=50)),
                ("stu_email", models.EmailField(max_length=254)),
                ("stu_dis", models.CharField(max_length=200)),
                ("stu_contact", models.IntegerField()),
                ("stu_dob", models.DateField()),
                ("stu_quali", models.CharField(max_length=50)),
                ("stu_gender", models.CharField(max_length=50)),
                ("stu_image", models.ImageField(upload_to="image/")),
                ("stu_file", models.FileField(upload_to="file/")),
                ("stu_password", models.CharField(max_length=15)),
            ],
        ),
    ]
