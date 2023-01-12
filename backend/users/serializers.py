from rest_framework import serializers
from .models import CustomUser, RequestUser, RequestUserImage, UserReview, PopularReview
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    telegram_username = serializers.CharField(max_length=56, validators=[UniqueValidator(
        queryset = CustomUser.objects.all(),
        message = "Пользователь с таким username уже существует."
    )])

    email = serializers.CharField(max_length=56, validators=[UniqueValidator(
        queryset = CustomUser.objects.all(),
        message = "Пользователь с таким email уже существует."
    )])

    email = serializers.EmailField(required=False)

    phone = serializers.CharField(max_length=28, validators=[UniqueValidator(
        queryset = CustomUser.objects.all(),
        message = "Пользователь с таким номером телефона уже существует."
    )])

    phone = serializers.CharField(required=False)

    def create(self, validated_data):
        # Хеширование пароля
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        validated_data["password"] = hashed_password
        # Сохранение изменений
        return CustomUser.objects.create(**validated_data)

    class Meta:
        model = CustomUser
        fields = ("url", "id", "is_active", "is_staff", "is_superuser", "first_name", "last_name", "username", "telegram_username", "password", "email", "avatar", "phone")

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
