# Generated by Django 2.2.4 on 2019-08-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quotes",
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
                ("title", models.CharField(max_length=200)),
                ("text", models.CharField(max_length=1000)),
                ("source", models.CharField(max_length=5)),
                ("bg_photo", models.ImageField(upload_to="images/%Y/%m/%d/")),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("name", models.CharField(max_length=100)),
                ("color", models.CharField(blank=True, max_length=100)),
                ("percentage", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
