from django.http import HttpResponseNotFound
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from .serializers import CreateItemSerializer
from adminn.models import Cars
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from django.shortcuts import get_object_or_404

@api_view(http_method_names=['GET'])
def index(request, pk=None, format=None):
    item = get_object_or_404(Cars, pk=pk)
    return Response({
        'create_user': reverse('create_user', request=request, format=format),
        'create_item': reverse('create_item', request=request, format=format),
        'user_dashboard': reverse('user_dashboard', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'detailed_view': reverse('detailed_view', kwargs={'pk': item.pk}, request=request, format=format),
    })
    
class CreateItem(CreateAPIView):
    serializer_class = CreateItemSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]