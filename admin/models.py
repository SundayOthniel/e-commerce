from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .utility import default_profile_image 


class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        user = self.model(email=email, password=password, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        email = email.capitalize()
        extra_fields['first_name'] = extra_fields['first_name'].capitalize()
        extra_fields['last_name'] = extra_fields['last_name'].capitalize()

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('is_active must have is_active=True.')
        else:
            user = self.create_user(email, password, **extra_fields)
            default_profile_image(user=user)
            return user


class Users(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UsersManager()

    class Meta:
        db_table = 'users'
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class ProfilePicture(models.Model):
    user = models.OneToOneField(
        Users, on_delete=models.CASCADE, related_name='user')
    profile_picture = models.ImageField(upload_to='media/profile_picture/')

    class Meta:
        db_table = 'profile_picture'


class Cars(models.Model):
    fuel_type = models.CharField(max_length=20, null=False, blank=False)
    # condition = models.CharField(max_length=5, null=False, blank=False)
    # millage = models.PositiveIntegerField(null=False, blank=False)
    # transmission = models.CharField(max_length=20, null=False, blank=False)
    # first_registration = models.CharField(max_length=255, default="Not registered", null=False, blank=False)
    # engine_power = models.PositiveIntegerField(null=False, blank=False)
    # description = models.TextField(null=False, blank=False)
    # interior_material = models.CharField(max_length=255, null=False, blank=False)
    # chases_id = models.PositiveIntegerField(null=False, blank=False)
    # category = models.CharField(max_length=20, null=False, blank=False)
    # brand = models.CharField(max_length=20, null=False, blank=False)
    # available  = models.CharField(max_length=3, default='Yes', null=False, blank=False)
    # car_model = models.CharField(max_length=20, null=False, blank=False)
    # price =  models.PositiveIntegerField(null=False, blank=False)
    # drive_type = models.PositiveIntegerField(null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-publish_date']
        db_table = 'cars'


class CarImage(models.Model):
    car = models.ForeignKey(Cars, related_name='images',
                            on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/car_images/')

    class Meta:
        db_table = 'car_image'

class CarThumbnail(models.Model):
    car = models.OneToOneField(Cars, on_delete=models.CASCADE, related_name='thumbnail')
    image = models.ImageField(upload_to='car_thumbnail')
    class Meta:
        db_table = 'car_thumbnail'