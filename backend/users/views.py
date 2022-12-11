from urllib import response
from rest_framework import viewsets, permissions
from .models import CustomUser, RequestUser, RequestUserImage
from .serializers import CustomUserSerializer, RequestUserSerializer, RequestUserImageSerializers

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class RequestUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RequestUser.objects.all()
    serializer_class = RequestUserSerializer
    permission_classes = [permissions.AllowAny]

class RequestUserImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RequestUserImage.objects.all()
    serializer_class = RequestUserImageSerializers
    permission_classes = [permissions.AllowAny]
