from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "password", "is_superuser", "telegram_username", "requests", "is_staff")
