# Generated by Django 4.1.7 on 2023-07-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RB_APP', '0015_alter_restaurant_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='approval_status',
            field=models.BooleanField(blank=True, choices=[(True, 'Approved'), (False, 'Not Approved')], null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owners',
            field=models.ManyToManyField(related_name='restaurant_owned', to='RB_APP.userdetails'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
