# Generated by Django 4.1.7 on 2023-08-28 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RB_APP', '0022_reservation_outside'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'RestaurantTypes',
            },
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='restaurants_owned', to='RB_APP.userdetails'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='restaurants_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Italian', 'איטלקי'), ('Mexican', 'מקסיקני'), ('Chinese', 'סיני'), ('Japanese', 'יפני'), ('Indian', 'הודי'), ('French', 'צרפתי'), ('Thai', 'תאילנדי'), ('Mediterranean', 'תיכוני'), ('Korean', 'קוריאני'), ('American', 'אמריקאי'), ('Greek', 'יווני'), ('Spanish', 'ספרדי'), ('Vietnamese', 'ויאטנמי'), ('Middle Eastern', 'מזרח תיכוני'), ('Brazilian', 'ברזילאי')], max_length=100)),
                ('restaurants', models.ManyToManyField(related_name='cuisines_list', to='RB_APP.restaurant')),
            ],
            options={
                'db_table': 'Cuisines',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rest_types',
            field=models.ManyToManyField(blank=True, null=True, related_name='type_restaurants', to='RB_APP.restauranttype'),
        ),
    ]
