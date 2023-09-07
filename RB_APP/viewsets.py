from django_filters.rest_framework import FilterSet
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
import django_filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserDetails, Cuisine, RestaurantType
from .models import Restaurant, Reservation, User
from .serializers import RestaurantSerializer, ReservationSerializer, UserSerializer, DetailedUserSerializer, \
    CuisineSerializer, RestaurantTypeSerializer, RestaurantOwnerSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class RestaurantFilterSet(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    cuisine_type = django_filters.CharFilter(lookup_expr='icontains')
    rest_types = django_filters.ModelMultipleChoiceFilter(
        field_name='rest_types',
        to_field_name='id',
        queryset=RestaurantType.objects.all(),
    )
    class Meta:
        model = Restaurant
        fields = []

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilterSet

    @action(detail=True, methods=['POST'])
    def add_owner(self, request, pk=None):
        restaurant = self.get_object()
        user_id = request.data.get('user_id')

        try:
            user_details = UserDetails.objects.get(user_id=user_id)
            restaurant.restaurant_owner = user_details.user
            restaurant.save()
            return Response({'message': 'Owner added successfully'})
        except UserDetails.DoesNotExist:
            return Response({'error': 'User details not found'}, status=400)



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
    permission_classes = [IsAuthenticated]



class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

class RestaurantTypeViewSet(viewsets.ModelViewSet):
    queryset = RestaurantType.objects.all()
    serializer_class = RestaurantTypeSerializer


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
    permission_classes = [IsAdminUser]

class RestaurantOwnerViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantOwnerSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    detailed_user = request.user.details  # Access the DetailedUser object associated with the authenticated user
    serializer = DetailedUserSerializer(instance=detailed_user, context={'request': request})
    return Response(data=serializer.data)



