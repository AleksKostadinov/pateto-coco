# Generated by Django 4.2 on 2023-04-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coco', '0014_alter_placesvisited_options_placesvisited_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placesvisited',
            name='date',
            field=models.DateField(),
        ),
    ]
