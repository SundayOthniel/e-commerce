from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('is_active must have is_active=True.')
        else:
            return self.create_user(
                email=email, password=password, **extra_fields.capitalize())


class Users(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
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


class ProfilePicture(models.Model):
    user = models.OneToOneField(
        Users, on_delete=models.CASCADE, related_name='user')
    profile_picture = models.ImageField(upload_to='profile_picture')

    class Meta:
        db_table = 'profile_picture'


class Cars(models.Model):
    fuel_type = models.CharField(max_length=20)
    condition = models.CharField(max_length=5)
    transmission = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    available  = models.CharField(max_length=3, default='Yes')
    car_model = models.CharField(max_length=20)
    price =  models.PositiveIntegerField()
    publish_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-publish_date']
        db_table = 'Cars'


class CarImage(models.Model):
    car = models.ForeignKey(Cars, related_name='images',
                            on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')

    class Meta:
        db_table = 'car_image'

class CarThumbnail(models.Model):
    car = models.OneToOneField(Cars, on_delete=models.CASCADE, related_name='thumbnail')
    image = models.ImageField(upload_to='car_thumbnail')
    class Meta:
        db_table = 'car_thumbnail'