# Generated by Django 4.1.7 on 2023-07-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RB_APP', '0007_alter_userdetails_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user_comment',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
