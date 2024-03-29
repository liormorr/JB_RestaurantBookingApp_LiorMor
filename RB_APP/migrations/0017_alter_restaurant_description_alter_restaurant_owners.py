# Generated by Django 4.1.7 on 2023-07-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RB_APP', '0016_alter_restaurant_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owners',
            field=models.ManyToManyField(blank=True, null=True, related_name='restaurant_owned', to='RB_APP.userdetails'),
        ),
    ]
