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



class DetailedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['phone_number']

class UserSerializer(serializers.ModelSerializer):
    details = DetailedUserSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'details']
        validators = [UniqueTogetherValidator(User.objects.all(), ['email'])]

    def create(self, validated_data):
        profile_details = validated_data.pop('details')
        user = User.objects.create_user(**validated_data)
        UserDetails.objects.create(user=user, **profile_details)
        return user