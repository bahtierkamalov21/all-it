from rest_framework import serializers
from .models import CustomUser, UserReview, PopularReview
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

    phone = serializers.CharField(max_length=28, validators=[UniqueValidator(
        queryset = CustomUser.objects.all(),
        message = "Пользователь с таким номером телефона уже существует."
    )])
    
    telegram_username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    
    def hashing_password(self, instance, validated_data, type):
        if type == "create":
            password = validated_data.pop("password")
            hashed_password = make_password(password)
            validated_data["password"] = hashed_password
        elif type == "update":
            password = validated_data.get("password", instance.password)
            hashed_password = make_password(password)
            instance.password = hashed_password

    def create(self, validated_data):
        # Хеширование пароля
        self.hashing_password(None, validated_data, "create")

        # Сохранение изменений
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Хеширование пароля
        self.hashing_password(instance, validated_data, "update")

        # Сохранение изменений
        for attr, value in validated_data.items():
            if attr not in ["password"]:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = [
            "url", 
            "id", 
            "is_active", 
            "is_staff", 
            "is_superuser", 
            "first_name", 
            "last_name", 
            "username", 
            "telegram_username", 
            "password", 
            "email", 
            "avatar", 
            "phone", 
            "review",
        ]

class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, validated_data):
        if self.context['request'].method == 'POST':
            if UserReview.objects.filter(fk_user=validated_data["fk_user"]).exists():
                raise serializers.ValidationError({"fk_user": "Пользователь может оставить только один отзыв."})
            return validated_data
        return validated_data

    class Meta:
        model = UserReview
        fields = '__all__'
        
class PopularReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PopularReview
        fields = '__all__'
