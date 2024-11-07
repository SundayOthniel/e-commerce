from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import ChangePasswordSerializer, CreateUserSerializer, LoginSerializer, UpdateProfileSerializer, UserDashboardSerializer
from adminn.models import Cars, Users
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
# from rest_framework import authentication
from django.contrib.auth import authenticate
from rest_framework import status
# from django.contrib.auth import update_session_auth_hash
from django_filters import rest_framework as filters
from .utility import token
from django.core.cache import cache


# Can be accessed by anyone
class CreateUser(ListCreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]
    
    
# Can be accessed by anyone
class Login(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            details = request.data
        except Exception as e:
            return Response({"Error": f"{e} occoured"})
        seralize_details = self.serializer_class(data=details)
        if seralize_details.is_valid(raise_exception=True):
            email = seralize_details.validated_data.get('email')
            password = seralize_details.validated_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                request.session["user"] = user.id
                refresh_token, access_token = token(user)
                response = Response({
                    'refresh': str(refresh_token),
                    'access': str(access_token),
                }, status=status.HTTP_200_OK)

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
                return Response(
                    {"error": "Invalid email or password"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(seralize_details.errors, status=status.HTTP_400_BAD_REQUEST)

# Can be accessed by User
class UserDashboard(ListAPIView):
    queryset = Cars.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDashboardSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('fuel_type', 'condition', 'transmission')

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        cache_key = f"user_dashboard_{request.GET.urlencode()}"
        cache_data = cache.get(cache_key)
        
        if cache_data:
            return Response(cache_data, status=status.HTTP_200_OK)
        if not queryset.exists():
            return Response(
                {"MatchError": "No match found"},
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60 * 60)  # Cache for 1 hour
            return Response(data, status=status.HTTP_200_OK)

# Can be accessed by User


class DetailedView(RetrieveAPIView):
    # permission_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    serializer_class = UserDashboardSerializer
    queryset = Cars.objects.all()

# Can be accessed by anyone


class UdateProfile(UpdateAPIView):
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer
    queryset = Users.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.pk != kwargs.get(self.lookup_field):
            return Response({"PermissionError": "You are trying to change another user\'s details"})
        else:
            return super().update(request, *args, **kwargs)

# Can be accessed by anyone


class ChangePassword(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            # update_session_auth_hash(request, request.user)
            return Response({"success": "Password changed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


