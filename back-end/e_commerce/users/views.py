from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView,RetrieveAPIView
from .serializers import CreateUserSerializer, LoginSerializer, UserDashboardSerializer
from adminn.models import Cars
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
# from rest_framework import authentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django_filters import rest_framework as filters


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
            raise ValueError({"Error": f"{e} error occoured"})
        seralize_details = self.serializer_class(data=details)
        if seralize_details.is_valid(raise_exception=True):
            email = seralize_details.validated_data.get('email')
            password = seralize_details.validated_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                if user.is_superuser:
                    pass
                    # redirect to admin page and assign a token
                    # then return response
                else:
                    refresh_token = RefreshToken.for_user(user)
                    access_token = refresh_token.access_token
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


class UserDashboard(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = UserDashboardSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'in_stock')
    
class DetailedView(RetrieveAPIView):
    # permission_classes = [JWTAuthentication]
    lookup_field = 'pk'
    serializer_class = UserDashboardSerializer
    queryset =  Cars.objects.all()