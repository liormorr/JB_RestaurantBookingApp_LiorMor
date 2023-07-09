from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from RB_APP.models import User, Reservation
from RB_APP.serializers import ReservationSerializer, WriteReservationSerializer, RestaurantSerializer


@api_view(['PUT'])
def create_reservation(request):
    full_data = request.data.copy()
    serializer = ReservationSerializer(data=full_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_reservation_information(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    serializer = WriteReservationSerializer(reservation)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_user(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    password = request.data.get('password')
    phone_number = request.data.get('phone_number')
    email_address = request.data.get('email_address')

    if not first_name or not last_name or not password or not phone_number or not email_address:
        return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create(first_name=first_name, last_name=last_name, password=password,
                                   phone_number=phone_number, email_address=email_address)
        return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)