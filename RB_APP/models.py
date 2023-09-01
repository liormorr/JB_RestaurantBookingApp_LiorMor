from django.core.validators import EmailValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class UserDetails(models.Model):
    phone_number = models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.RESTRICT,related_name='details')


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'DetailedUser'



class Restaurant(models.Model):
    APPROVAL_CHOICES = [
        (True, 'Approved'),
        (False, 'Not Approved'),
    ]

    name = models.CharField(max_length=256)
    description = models.TextField(max_length=800)
    location = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    approval_status = models.BooleanField(choices=APPROVAL_CHOICES, null=True, blank=True)
    restaurant_owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.RESTRICT,
                                         related_name='restaurants_owned')
    phone_number = models.CharField(max_length=20)
    facebook_link = models.URLField(max_length=500, null=True, blank=True)
    instagram_link = models.URLField(max_length=500, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    logo = models.URLField(max_length=1000, null=True, blank=True)
    rest_picture = models.URLField(max_length=1000, null=True, blank=True)
    owners = models.ManyToManyField(UserDetails, related_name='restaurants_owned', blank=True)
    rest_types = models.ManyToManyField('RestaurantType', related_name='type_restaurants', blank=True)
    cuisine_type = models.ManyToManyField('Cuisine', related_name='cuisines_list', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Restaurants'
        ordering = ['id']

class RestaurantType(models.Model):
    type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'RestaurantTypes'


class Cuisine(models.Model):
    ALLOWED_CUISINES = (
        ('איטלקי', 'Italian'),
        ('מקסיקני', 'Mexican'),
        ('סיני', 'Chinese'),
        ('יפני', 'Japanese'),
        ('הודי', 'Indian'),
        ('צרפתי', 'French'),
        ('תאילנדי', 'Thai'),
        ('תיכוני', 'Mediterranean'),
        ('קוריאני', 'Korean'),
        ('אמריקאי', 'American'),
        ('יווני', 'Greek'),
        ('ספרדי', 'Spanish'),
        ('ויאטנמי', 'Vietnamese'),
        ('מזרח תיכוני', 'Middle Eastern'),
        ('ברזילאי', 'Brazilian'),
        ('ארגנטינאי', 'Argentinian'),
    )
    name = models.CharField(max_length=100, choices=ALLOWED_CUISINES)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Cuisines'

class Reservation(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.RESTRICT, db_column='restaurant_id')
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, db_column='user_id')
    reservation_date = models.DateField(null=False, blank=False)
    reservation_time = models.TimeField(null=False, blank=False)
    request_creation = models.DateTimeField(auto_now_add=True)
    user_comment = models.CharField(max_length=256, null=True, blank=True)
    party_size = models.PositiveIntegerField(null=False, blank=False, validators=[MinValueValidator(1)])
    is_smoking = models.BooleanField(null=True, blank=True)
    bar = models.BooleanField(null=True, blank=True)
    outside = models.BooleanField(null=True, blank=True)
    approved = models.BooleanField(null=True, blank=True)
    table = models.ForeignKey('Table', null=True, blank=True, on_delete=models.RESTRICT)


    def __str__(self):
        return f"{self.user_id} {self.restaurant_id} {self.reservation_date} {self.reservation_time}"

    class Meta:
        db_table = 'Reservations'
        ordering = ['user_id']


class Table(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.RESTRICT, db_column='restaurant_id')
    seats_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    is_inside = models.BooleanField(null=True, blank=True)
    smoker = models.BooleanField(null=True, blank=True)
    bar = models.BooleanField(null=True, blank=True)
    near_window = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'Table'
        ordering = ['id']


