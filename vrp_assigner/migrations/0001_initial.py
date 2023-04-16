# Generated by Django 4.2 on 2023-04-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VrpLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("countryCode", models.CharField(default="D", max_length=30)),
                ("country", models.CharField(default="Deutschland", max_length=30)),
                ("cityCode", models.CharField(default="B", max_length=30)),
                ("city", models.CharField(default="Berlin", max_length=30)),
            ],
        ),
    ]
