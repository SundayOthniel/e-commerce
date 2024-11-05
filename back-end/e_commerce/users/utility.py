from django.conf import settings
from adminn.models import ProfilePicture
import os
from django.core.files import File

def default_profile_image(user=None):
        image_path = os.path.join(
            settings.BASE_DIR, 'users', 'static', 'default-avatar.jpg')
        if not os.path.exists(image_path):
            raise FileNotFoundError('Default image not found')
        else:
            with open(image_path, 'rb') as image:
                profile_image = File(image, name='default_profile_picture.jpg')
                ProfilePicture.objects.update_or_create(
                    user=user, defaults={'profile_picture': profile_image})