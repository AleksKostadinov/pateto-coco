# Generated by Django 4.2 on 2023-04-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coco', '0005_alter_post_destination_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]