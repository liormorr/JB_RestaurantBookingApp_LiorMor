from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
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

class UserSerializer(ModelSerializer):

    password = serializers.CharField(
        max_length=128, validators=[validate_password], write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'email': {'required': True},
            'username': {'read_only': True},

        }
        validators = [UniqueTogetherValidator(User.objects.all(), ['email'])]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['email'],
                                   email=validated_data['email'],
                                   first_name=validated_data.get('first_name', ''),
                                   last_name=validated_data.get('last_name', ''))
        user.set_password(validated_data['password'])
        user.save()
        return user