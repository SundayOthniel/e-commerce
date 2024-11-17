from rest_framework.reverse import reverse
from rest_framework import serializers
from adminn.models import Cars, CarImage, CarThumbnail, Users
from .utility import default_profile_image


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
        ]

    def validate_email(self, email_value):
        if Users.objects.filter(email=email_value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists.")
        else:
            return email_value

    def create(self, validated_data):
        user = Users.objects.create_user(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name').capitalize(),
            last_name=validated_data.get('last_name').capitalize(),
            password=validated_data.get('password'),
        )
        default_profile_image(user=user)
        return user

    def to_representation(self, instance):
        return {"detail": "User created successfully."}


class CarThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarThumbnail
        fields = ["image"]


class AllCarSerializer(serializers.ModelSerializer):
    thumbnail = CarThumbnailSerializer(read_only=True)
    # car_detail = serializers.HyperlinkedIdentityField(
    #     view_name='users:detailed_view', lookup_field='pk')

    class Meta:
        model = Cars
        exclude = ["publish_date"]


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["image"]


class CarsDetailsSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    # all_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cars
        exclude = ["publish_date"]
    # def get_all_cars(self, obj):
    #     request = self.context.get('request')
    #     return reverse('users:all_cars', request=request)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['email', 'password']

class UpdateProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
        ]
    def update(self, instance, validated_data):
        if not self.context['request'].user:
            raise LookupError
        else:
            instance.first_name = validated_data.get('first_name', instance.first_name).capitalize()
            instance.last_name = validated_data.get('last_name', instance.last_name).capitalize()
            instance.save()
            return instance
        
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    # repeat_new_password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['old_password',  'new_password', 'repeat_new_password']
    def validate(self, value):
        user = self.context['request'].user
        old_password = value.get('old_password')
        # new_password = value.get('new_password')
        # repeat_new_password = value.get('repeat_new_password')

        if not user.check_password(old_password):
            raise {"detail": "Old password is incorrect."}
        # if new_password != repeat_new_password:
        #     raise {"detail": "New passwords do not match."}
        else:
            return value

    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password']
        user.set_password(new_password)  # Hash the new password
        user.save() 