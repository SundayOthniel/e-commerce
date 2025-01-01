from django.urls import path
from .views import ChangePassword, Login, UpdateProfile, AllCar, CreateUser, DetailedView
from admin.utility import CustomTokenRefreshSlidingView



urlpatterns = [
    path('create_user', CreateUser.as_view(), name='create_user'),
    path('cars', AllCar.as_view(), name='all_cars'),
    path('login', Login.as_view(), name='login'),
    path('access_token', CustomTokenRefreshSlidingView.as_view(), name='access_token'),
    path('car/details/<int:pk>', DetailedView.as_view(), name='detailed_view'),
    path('update_profile/<int:pk>', UpdateProfile.as_view(), name='update_profile'),
    path('change_password', ChangePassword.as_view(), name='change_password'),
] 