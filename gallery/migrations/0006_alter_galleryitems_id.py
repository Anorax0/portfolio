# Generated by Django 3.2.12 on 2022-03-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_galleryitems_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitems',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
