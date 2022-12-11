from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueTogetherValidator

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "password", "is_superuser", "telegram_username", "requests", "is_staff")
        validators = [
            UniqueTogetherValidator(
                queryset=CustomUser.objects.all(),
                message="Этот telegram username занят, пожалуйста введите уникальный username",
                fields=['telegram_username']
            )
        ]
