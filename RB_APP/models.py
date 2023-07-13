from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from phonenumber_field.formfields import PhoneNumberField


class UserDetails(models.Model):
    phone_number = PhoneNumberField()
    user = models.OneToOneField(User,on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'DetailedUser'


class Restaurant(models.Model):
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    description = models.TextField(max_length=356, db_column='description', null=False, blank=False)
    location = models.CharField(max_length=256, db_column='location', null=False, blank=False)
    address = models.CharField(max_length=256, db_column='address', null=False, blank=False)
    approval_status = models.BooleanField(null=True, blank=True)
    restaurant_owner = models.ForeignKey(User,null=True, blank=True, on_delete=models.RESTRICT)
    phone_number = models.CharField(max_length=20, db_column='phone_number', null=False, blank=False)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    instagram_link = models.URLField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Restaurants'


class Reservation(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.RESTRICT, db_column='restaurant_id')
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, db_column='user_id')
    reservation_date = models.DateField(null=False, blank=False)
    reservation_time = models.TimeField(null=False, blank=False)
    request_creation = models.DateTimeField(auto_now_add=True)
    user_comment = models.CharField(max_length=256)
    party_size = models.PositiveIntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    is_smoking = models.BooleanField(null=True, blank=True)
    approved = models.BooleanField(null=True, blank=True)
    table_id = models.SmallIntegerField(null=True, blank=True)



    def __str__(self):
        return f"{self.user_id} {self.restaurant_id} {self.reservation_date} {self.reservation_time}"

    class Meta:
        db_table = 'Reservations'
