from django.urls import path
from .views import ChangePassword, Login, UdateProfile, UserDashboard, CreateUser, DetailedView
from .utility import CustomTokenRefreshSlidingView



urlpatterns = [
    path('create_user', CreateUser.as_view(), name='create_user'),
    path('user_dashboard', UserDashboard.as_view(), name='user_dashboard'),
    path('login', Login.as_view(), name='login'),
    path('access_token', CustomTokenRefreshSlidingView.as_view(), name='access_token'),
    path('detailed_view/<int:pk>', DetailedView.as_view(), name='detsiled_view'),
    path('update_profile/<int:pk>', UdateProfile.as_view(), name='update_profile'),
    path('change_password', ChangePassword.as_view(), name='change_password'),
] 