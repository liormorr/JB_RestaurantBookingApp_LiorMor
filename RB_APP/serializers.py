from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from RB_APP.models import Reservation, User, Restaurant, UserDetails


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class WriteReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        depth = 1


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'



class DetailedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, validators=[validate_password], write_only=True)
    phone_number = serializers.CharField(
        required=True, max_length=256, write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'read_only': True},
        }
        validators = [UniqueTogetherValidator(User.objects.all(), ['email'])]

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                username=validated_data['email'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''))
            UserDetails.objects.create(user=user, phone_number=validated_data['phone_number'])
        return user