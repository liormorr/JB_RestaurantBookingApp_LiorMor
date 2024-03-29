# Generated by Django 4.1.7 on 2023-07-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RB_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='approval_status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(db_column='description', max_length=356),
        ),
    ]
