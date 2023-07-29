"""JB_RestaurantBookingApp_LiorMor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from RB_APP.views import create_user, create_reservation, create_restaurant
from RB_APP.viewsets import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
path('api/create/user/', create_user, name='create_user'),
path('api/create/reservation/', create_reservation, name='create_reservation'),
path('api/create/restaurant/', create_restaurant, name='create_restaurant'),
path('api/auth/login', TokenObtainPairView().as_view()),
path('api/auth/signup', create_user, name='create_user'),
path('user-details/', UserViewSet.as_view(), name='user-details-list'),
path('user-details/<int:pk>/', UserViewSet.as_view, name='user-details-detail'),
]
