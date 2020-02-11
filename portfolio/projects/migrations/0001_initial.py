# Generated by Django 2.2.4 on 2019-08-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.URLField()),
                ('is_published', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]