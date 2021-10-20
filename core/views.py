from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, permissions, viewsets
from .serializers import UserDataSerializer, RegisterSerializer, UserSerializer
from .models import UserModel
from rest_framework.response import Response
import requests


def get_ip(request):
    adress = request.META.get('HTTP_X_FORWARDED_FOR')
    if adress:
        ip = adress.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_geolocation(request):
    access_key = 'd479f51305bbe0eface1532fecf88001'
    ip = get_ip(request)
    url = f"http://api.ipstack.com/{ip}?access_key={access_key}"
    response = requests.get(url)
    response.raise_for_status()
    rawData = response.json()
    ip = rawData['ip']
    continent_name = rawData['continent_name']
    country_name = rawData['country_name']
    region_name = rawData['region_name']
    city = rawData['city']
    zip = rawData['zip']
    latitude = rawData['latitude']
    longitude = rawData['longitude']
    saveNow = UserModel(
        continent_name=continent_name,
        country_name=country_name,
        region_name=region_name,
        city=city,
        zip=zip,
        latitude=latitude,
        longitude=longitude,
    )
    saveNow.save()
    api_response = {
        'continent_name': continent_name,
        'country_name': country_name,
        'region_name': region_name,
        'zip': zip,
        'latitude': latitude,
        'longitude': longitude,
    }
    return JsonResponse(api_response)


def get_geolocation_input_ip(request, ip_input):
    access_key = 'd479f51305bbe0eface1532fecf88001'
    url = f"http://api.ipstack.com/{ip_input}?access_key={access_key}"
    response = requests.get(url)
    response.raise_for_status()
    rawData = response.json()
    ip = rawData['ip']
    continent_name = rawData['continent_name']
    country_name = rawData['country_name']
    region_name = rawData['region_name']
    city = rawData['city']
    zip = rawData['zip']
    latitude = rawData['latitude']
    longitude = rawData['longitude']
    saveNow = UserModel(
        continent_name=continent_name,
        country_name=country_name,
        region_name=region_name,
        city=city,
        zip=zip,
        latitude=latitude,
        longitude=longitude,
    )
    saveNow.save()
    api_response = {
        'continent_name': continent_name,
        'country_name': country_name,
        'region_name': region_name,
        'zip': zip,
        'latitude': latitude,
        'longitude': longitude,
    }
    return JsonResponse(api_response)


class AllUsersView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [permissions.AllowAny]


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created",
        })


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args,  **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })
