from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from .models import Cars, Users
from .serializers import CreateItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, status
from django.core.cache import cache

@api_view(http_method_names=['GET'])
def index(request, format=None):
    user = Users.objects.first()
    car = Cars.objects.first()
    
    user_id = user.id if user else None
    car_id = car.id if car else None

    return Response({
        'create_item': reverse('create_item', request=request, format=format),
        'refresh_token': reverse('refresh_token', request=request, format=format),
        'create_user': reverse('create_user', request=request, format=format),
        'all_cars': reverse('all_cars', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'change_password': reverse('change_password', request=request, format=format),
        'detailed_view': reverse('detailed_view', kwargs={'pk': user_id}, request=request, format=format) if user_id else None,
        'update_profile': reverse('update_profile', kwargs={'pk': car_id}, request=request, format=format) if car_id else None
    })

    
class CreateItem(CreateAPIView):
    serializer_class = CreateItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            cache_key = f"all_cars_{request.GET.urlencode()}"
            cache.delete(cache_key)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)