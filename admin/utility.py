import cloudinary.uploader
from django.conf import settings
from rest_framework import status
import os
from django.core.files import File
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView


def default_profile_image(user=None):
    from .models import ProfilePicture
    
    image_path = os.path.join(
        settings.BASE_DIR, 'users', 'static', 'default-avatar.jpg')
    if not os.path.exists(image_path):
        raise FileNotFoundError('Default image not found')
    else:
        with open(image_path, 'rb') as image:
            profile_image = File(image, name='default_profile_picture.jpg')
            ProfilePicture.objects.update_or_create(
                user=user, defaults={'profile_picture': profile_image})
def token(user):
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token
    return refresh_token, access_token

class CustomTokenRefreshSlidingView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            access_token = response.data.get('access')

            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='Lax'
            )
        return response
    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def image_thumbnail_upload(image):
    thumbnail_upload = cloudinary.uploader.upload(
        image[0],
        folder="car_thumbnails",
        overwrite=True,
        resource_type="image"
    )
    
def car_images(images):
    image_upload = cloudinary.uploader.upload(
        images,
        folder="car_images",
        overwrite=True,
        resource_type="image"
    )