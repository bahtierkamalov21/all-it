from rest_framework import serializers
from .models import CustomUser, RequestUser, RequestUserImage
from rest_framework.validators import UniqueValidator

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    telegram_username = serializers.CharField(max_length=56, validators=[UniqueValidator(
        queryset = CustomUser.objects.all(),
        message = "Пользователь с таким username уже существует."
    )])

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "username", "password", "is_superuser", "telegram_username", "is_staff")

class RequestUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestUser
        fields = ("fk_user", "title", "name", "stack", "images")

class RequestUserImageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestUserImage
        fields = ("fk_request_user", "title", "image")
