from django.db import models
from django.core.validators import EmailValidator, MinValueValidator


class User(models.Model):
    first_name = models.CharField(max_length=256, db_column='first_name', null=False, blank=False)
    last_name = models.CharField(max_length=256, db_column='last_name', null=False, blank=False)
    password = ()
    phone_number = models.CharField(max_length=256, db_column='phone_number', null=False, blank=False)
    email_address = models.EmailField(max_length=256,db_column='email_address',null=True, blank=True, validators=EmailValidator)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'users'


class Restaurant(models.Model):
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    description = models.TextField(max_length=256, db_column='description', null=False, blank=False)
    location = models.CharField(max_length=256, db_column='location', null=False, blank=False)
    address = models.CharField(max_length=256, db_column='address', null=False, blank=False)
    approval_status = models.BooleanField(null=False, blank=False)
    phone_number = models.CharField(max_length=20, db_column='phone_number', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Restaurants'



class Reservation(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, db_column='restaurant_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    reservation_date = models.DateField(null=False, blank=False)
    reservation_time = models.TimeField(null=False, blank=False)
    request_creation = models.DateTimeField(auto_now_add=True)
    user_comment = models.CharField(max_length=256)
    party_size = models.PositiveIntegerField(null=False, blank=False, validators=[MinValueValidator(1)])


