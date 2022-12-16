from rest_framework import serializers
from .models import CustomUser, RequestUser, RequestUserImage, UserReview
from rest_framework.validators import UniqueValidator
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAuthenticatedOrAdminOrReadOnly

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    telegram_username = serializers.CharField(max_length=56, validators=[UniqueValidator(
        queryset = CustomUser.objects.all(),
        message = "Пользователь с таким username уже существует."
    )])

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "username", "telegram_username", "password", "requests")
        permission_classes = (IsAuthenticatedOrAdminOrReadOnly)

class RequestUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestUser
        fields = ("fk_user", "title", "name", "stack", "images")
        permission_classes = (IsAuthenticated)

class RequestUserImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestUserImage
        fields = ("fk_request_user", "title", "image")
        permission_classes = (IsAuthenticated)

class UserReviewSerializer(serializers.HyperlinkedModelSerializer):
    fk_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserReview
        fields = ("fk_user", "date", "message", "rating")
        permission_classes = (IsAuthenticatedOrReadOnly)
