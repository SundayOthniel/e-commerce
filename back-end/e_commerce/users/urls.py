from django.urls import path
from .views import ChangePassword, Login, UdateProfile, UserDashboard, CreateUser, DetailedView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('create_user', CreateUser.as_view(), name='create_user'),
    path('user_dashboard', UserDashboard.as_view(), name='user_dashboard'),
    path('login', Login.as_view(), name='login'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('detailed_view/<int:pk>/', DetailedView.as_view(), name='detsiled_view'),
    path('update_profile/<int:pk>/', UdateProfile.as_view(), name='update_profile'),
    path('change_password', ChangePassword.as_view(), name='change_password'),
] 