# Generated by Django 4.1.7 on 2023-08-04 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RB_APP', '0018_restaurant_logo_restaurant_rest_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rest_picture',
        ),
    ]