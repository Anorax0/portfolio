# Generated by Django 2.2.4 on 2019-10-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_darkskyapi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='darkskyapi',
            options={'verbose_name': 'Weather Data', 'verbose_name_plural': 'Weather Data'},
        ),
        migrations.AlterField(
            model_name='darkskyapi',
            name='forecast_date',
            field=models.DateTimeField(default='2019-10-03'),
        ),
    ]