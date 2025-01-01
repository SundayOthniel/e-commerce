from django.urls import path
from .views import CreateItem, index
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', index, name='index'),
    path('create_item', CreateItem.as_view(), name='create_item'),
    path('refresh_token', TokenRefreshView.as_view(), name='refresh_token'),
]