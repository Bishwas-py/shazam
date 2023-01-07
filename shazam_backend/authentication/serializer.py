from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from authentication.models import Status, Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, validators=[validate_password])
    password_confirmation = serializers.CharField(max_length=128, min_length=8, write_only=True)

    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirmation']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username already exists.")
        if not value.isalnum():
            raise serializers.ValidationError("The username should only contain alphanumeric characters.")
        if value.lower() in ['admin', 'root', 'user', 'superuser', 'super', 'moderator', 'mod', 'codie']:
            raise serializers.ValidationError("This username is restricted, please try another one.")

        return value

    def validate_password_confirmation(self, value):
        data = self.get_initial()
        password = data.get('password')
        password_confirmation = value

        if password != password_confirmation:
            raise serializers.ValidationError("Confirmation password does not match with password.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        return user


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['is_confirmed', 'token_key_expires', 'last_sent_time']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'image']


# user data serializer
class UserSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_staff', 'is_superuser', 'is_active',
            'status', 'profile'
        ]
