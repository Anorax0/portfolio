# Generated by Django 2.2.4 on 2019-09-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryitems',
            options={'verbose_name_plural': 'Gallery Items'},
        ),
        migrations.AlterField(
            model_name='galleryitems',
            name='image',
            field=models.ImageField(upload_to='images/meme'),
        ),
    ]
