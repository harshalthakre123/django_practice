# Generated by Django 5.2 on 2025-05-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_alter_vehicle_vehicle_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ht",
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
            ],
        ),
    ]
