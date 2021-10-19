from django.urls import path, include
from .views import get_geolocation, get_ip, get_geolocation_input_ip, AllUsersView, RegisterView, ProfileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', AllUsersView, basename='users')

urlpatterns = [
    path("", get_geolocation, name='get_geolocation'),
    path("ip/<str:ip_input>/", get_geolocation_input_ip, name='get_geolocation_input_ip'),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("", include(router.urls))
]