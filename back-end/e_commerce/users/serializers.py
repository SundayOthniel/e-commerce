from rest_framework import serializers
from adminn.models import Cars, Users
from .utility import default_profile_image


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    comfirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'comfirm_password',
        ]

    def validate(self, value):
        if not value['password'] == value['comfirm_password']:
            raise serializers.ValidationError("Password mismatch")
        else:
            return value

    def validate_email(self, email_value):
        if Users.objects.filter(email=email_value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists.")
        return email_value

    def create(self, validated_data):
        user = Users.objects.create_user(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password'),
        )
        default_profile_image(user=user)
        return user


class UserDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['email', 'password']
