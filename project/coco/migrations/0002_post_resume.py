# Generated by Django 4.2 on 2023-04-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resume',
            field=models.CharField(default=' ', max_length=500),
            preserve_default=False,
        ),
    ]