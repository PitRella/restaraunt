from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, CharField, EmailField
from user.models import CustomUser
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserOutSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'avatar')
        read_only_fields = ('email',)


class UserRegisterSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    retype_password = CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "avatar", "password", "retype_password")
        read_only_fields = ("email",)

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Этот email уже зарегистрирован.")
        return value

    def validate(self, data):
        password = data.get("password")
        retype_password = data.get("retype_password")

        if password != retype_password:
            raise ValidationError({"retype_password": "Пароли не совпадают."})

        validate_password(password)

        return data

    def create(self, validated_data):
        validated_data.pop("retype_password")
        user = CustomUser.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token obtain serializer to get token based not only on ID, also on email."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
