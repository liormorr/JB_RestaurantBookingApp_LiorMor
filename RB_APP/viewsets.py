from django_filters.rest_framework import FilterSet
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
import django_filters
from .models import UserDetails
from .models import Restaurant, Reservation, User
from .serializers import RestaurantSerializer, ReservationSerializer, UserSerializer, DetailedUserSerializer


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



class UserDetailsFilter(django_filters.FilterSet):
    phone_number = django_filters.CharFilter(lookup_expr='icontains')
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    first_name = django_filters.CharFilter(field_name='user__first_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='user__last_name', lookup_expr='icontains')

    class Meta:
        model = UserDetails
        fields = ['phone_number', 'username', 'first_name', 'last_name']

class UserViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = UserDetails.objects.all()
    serializer_class = DetailedUserSerializer
    filterset_class = UserDetailsFilter




