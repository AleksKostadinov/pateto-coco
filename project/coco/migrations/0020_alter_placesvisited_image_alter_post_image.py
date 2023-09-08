# Generated by Django 4.2.3 on 2023-09-08 08:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coco', '0019_alter_placesvisited_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placesvisited',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]
