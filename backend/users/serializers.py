from rest_framework import serializers
from .models import CustomUser, RequestUser, RequestUserImage, UserReview, PopularReview
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    telegram_username = serializers.CharField(max_length=56, validators=[UniqueValidator(
        queryset = CustomUser.objects.all(),
        message = "Пользователь с таким username уже существует."
    )])

    def create(self, validated_data):
        # Хеширование пароля
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        validated_data["password"] = hashed_password
        return CustomUser.objects.create(**validated_data)

    class Meta:
        model = CustomUser
        fields = ("url", "is_active", "first_name", "last_name", "username", "telegram_username", "password", "avatar")

class RequestUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestUser
        fields = '__all__'

class RequestUserImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestUserImage
        fields = '__all__'

class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserReview
        fields = '__all__'
        
class PopularReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PopularReview
        fields = '__all__'
