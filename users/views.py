from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import CarsDetailsSerializer, ChangePasswordSerializer, CreateUserSerializer, LoginSerializer, UpdateProfileSerializer, AllCarSerializer
from admin.models import Cars, Users
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework import status
from django_filters import rest_framework as filters
from admin.utility import get_client_ip, token
from django.core.cache import cache
from rest_framework.renderers import JSONRenderer
# from rest_framework.exceptions import AnonRateThrottle
from rest_framework.throttling import AnonRateThrottle

import logging
logger = logging.getLogger(__name__)


# Can be accessed by anyone
class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

# Can be accessed by anyone
# Done
class Login(APIView):
    renderer_classes = [JSONRenderer]
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]
    
    def post(self, request, format=None):
        try:
            details = request.data
        except Exception as e:
            return Response({"detail": f"{e} occoured"})
        seralize_details = self.serializer_class(data=details)
        if seralize_details.is_valid(raise_exception=True):
            email = seralize_details.validated_data.get('email').capitalize()
            password = seralize_details.validated_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                logger.info(f'{user.first_name.capitalize()} just made a successfull login')
                refresh_token, access_token = token(user)
                response = Response({"detail":"Successfully login"},status=status.HTTP_200_OK)
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh_token),
                    httponly=True,
                    secure=True,
                    samesite='Lax',
                )

                response.set_cookie(
                    key='access_token',
                    value=str(access_token),
                    httponly=True,
                    secure=True,
                    samesite='Lax',
                )

                return response
            else:
                ip = get_client_ip(request)
                logger.warning(f'{request.user} with ip({ip}) failed to login due to bad credentials...')
                return Response(
                    {"detail": "Invalid email or password"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(seralize_details.errors, status=status.HTTP_400_BAD_REQUEST)


# Can be accessed by anyone

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    condition = filters.CharFilter(field_name="condition", lookup_expr='iexact')
    brand = filters.CharFilter(field_name="brand", lookup_expr='iexact')
    car_model = filters.CharFilter(field_name="car_model", lookup_expr='iexact')
    category = filters.CharFilter(field_name="category", lookup_expr='iexact')
    available = filters.BooleanFilter(field_name="available", lookup_expr='iexact')
    fuel_type = filters.CharFilter(field_name="fuel_type", lookup_expr='iexact')

    class Meta:
        model = Cars
        fields = ['condition', 'brand', 'car_model', 'category', 'available', 'fuel_type']
        
class AllCar(ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Cars.objects.all()
    serializer_class = AllCarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class  = ProductFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        cache_key = f"cars_{request.GET.urlencode()}"
        cache_data = cache.get(cache_key)
        
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)
        if queryset:
            queryset_serializer = self.get_serializer(queryset, many=True)
            data = queryset_serializer.data
            cache.set(cache_key, data, timeout=60 * 60)
            print(f"Cached: {cache_key}")
            return Response(data, status=status.HTTP_200_OK)
            
        else:
            return Response(
                {"detail": "Not available..."},
                status=status.HTTP_404_NOT_FOUND
            )
        
# Can be accessed by Users or admin
class DetailedView(RetrieveAPIView):
    authention_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    serializer_class = CarsDetailsSerializer
    queryset = Cars.objects.all()

    def get(self, request, *args, **kwargs):
        cache_key = f"car_detail_{kwargs[self.lookup_field]}"
        cache_data = cache.get(cache_key)
        
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)
        else:
            car_detail = self.get_object()
            car_detail_serializer = self.get_serializer(car_detail)
            car_data = car_detail_serializer.data
            cache.set(cache_key, car_data, timeout=60 * 60)
            return Response(car_data, status=status.HTTP_200_OK)

# Can be accessed by either admin or users
class UpdateProfile(UpdateAPIView):
    lookup_field = 'pk'
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer
    queryset = Users.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.handle_update(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.handle_update(request, *args, **kwargs)
    
    def handle_update(self, request, *args, **kwargs):
        user = request.user
        if user.pk != kwargs.get(self.lookup_field):
            return Response({"detail": "You are trying to change another user\'s details"})
        else:
            return super().update(request, *args, **kwargs)

# Can be accessed by either admin or users
class ChangePassword(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            # update_session_auth_hash(request, request.user)
            return Response({"detail": "Password changed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

async def me(request):
    return await Response({"hi":"Hi"})