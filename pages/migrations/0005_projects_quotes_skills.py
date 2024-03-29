# Generated by Django 2.2.4 on 2019-09-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_auto_20190912_2031"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
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
                ("description", models.TextField()),
                ("address", models.URLField()),
                ("is_published", models.BooleanField(default=False)),
                ("date", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
            },
        ),
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
            options={
                "verbose_name": "Quote",
                "verbose_name_plural": "Quotes",
            },
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
                ("is_published", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Skill",
                "verbose_name_plural": "Skills",
            },
        ),
    ]
