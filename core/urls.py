from django.urls import path, include
from .views import get_geolocation, get_ip, AllUsersView, GetUserView, RegisterView, ProfileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', AllUsersView, basename='users')

urlpatterns = [
    path("", get_geolocation, name='get_geolocation'),
    path("user/", GetUserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("", include(router.urls))
]