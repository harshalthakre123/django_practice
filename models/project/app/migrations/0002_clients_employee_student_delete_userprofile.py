# Generated by Django 5.2 on 2025-04-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clients",
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
                ("name", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=255, unique=True),
                ),
                ("contact", models.IntegerField(max_length=10)),
                ("project", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=255, unique=True),
                ),
                ("contact", models.IntegerField(max_length=10)),
                ("department", models.CharField(max_length=50)),
                ("salary", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
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
                ("name", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=255, unique=True),
                ),
                ("contact", models.IntegerField(max_length=10)),
                ("branch", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
