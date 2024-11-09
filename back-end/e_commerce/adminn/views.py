from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from .serializers import CreateItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, status
from django.core.cache import cache

@api_view(http_method_names=['GET'])
def index(request, format=None):
    return Response({
        'create_user': reverse('create_user', request=request, format=format),
        'create_item': reverse('create_item', request=request, format=format),
        'all_cars': reverse('all_cars', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'change_password': reverse('change_password', request=request, format=format),
    })
    
class CreateItem(CreateAPIView):
    serializer_class = CreateItemSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            cache_key = f"all_cars_{request.GET.urlencode()}"
            cache.delete(cache_key)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Erroe":"Invalid"}, status=status.HTTP_400_BAD_REQUEST)