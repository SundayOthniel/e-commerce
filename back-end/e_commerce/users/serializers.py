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
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.save()
            return instance
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    repeat_new_password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['old_password',  'new_password', 'repeat_new_password']
    def validate(self, value):
        user = self.context['request'].user
        old_password = value.get('old_password')
        new_password = value.get('new_password')
        repeat_new_password = value.get('repeat_new_password')

        if not user.check_password(old_password):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})
        if new_password != repeat_new_password:
            raise serializers.ValidationError({"repeat_new_password": "New passwords do not match."})
        else:
            return value

    def save(self):
        user = self.context['request'].user
        new_password = self.validated_data['new_password']
        user.set_password(new_password)  # Hash the new password
        user.save() 