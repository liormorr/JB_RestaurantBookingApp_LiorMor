from django_filters.rest_framework import FilterSet
from rest_framework import viewsets
from .models import Restaurant, Reservation, User
from .serializers import RestaurantSerializer, ReservationSerializer, UserSerializer


class RestaurantFilterSet(FilterSet):
    class Meta:
        model = Restaurant
        fields = {
            'name': ['exact', 'icontains'],
            'location': ['exact', 'icontains'],
            'approval_status': ['exact'],
        }

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilterSet



class ReservationFilterSet(FilterSet):
    class Meta:
        model = Reservation
        fields = {
            'restaurant_id': ['exact'],
            'user_id': ['exact'],
            'reservation_date': ['exact', 'gte', 'lte'],
            'reservation_time': ['exact', 'gte', 'lte'],
            'approved': ['exact'],
        }

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filterset_class = ReservationFilterSet


class UserFilterSet(FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'phone_number': ['exact'],
            'email_address': ['exact', 'icontains'],
        }

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilterSet




