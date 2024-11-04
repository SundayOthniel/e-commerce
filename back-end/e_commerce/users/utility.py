from django.conf import settings
from adminn.models import ProfilePicure
import os
from django.core.files import File

def default_profile_image(self, user=None):
        image_path = os.path.join(
            settings.BASE_DIR, 'users', 'static', 'default-avatar.jpg')
        if not os.path.exists(image_path):
            raise FileNotFoundError('Default image not found')
        else:
            with open(image_path, 'rb') as image:
                profile_image = File(image, name='default_profile_picture.jpg')
                ProfilePicure.objects.update_or_create(
                    user=user, defaults={'profile_picture': profile_image})

def pro_imag(user):
    path = os.path.join('users', 'static', 'default-avartar.jpg')
    if not os.path.exists(path):
        raise FileNotFoundError('path not found')
    else:
        with open(path, 'rb') as img:
            profile_picture = File(img, name='default_img.png')
            pro_img = ProfilePicure.objects.create(user=user, profile_picture=profile_picture)
            return pro_img