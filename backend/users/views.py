from urllib import response
from rest_framework import viewsets, permissions
from .models import CustomUser, RequestUser, RequestUserImage, UserReview, PopularReview
from .serializers import CustomUserSerializer, RequestUserSerializer, RequestUserImageSerializer, UserReviewSerializer, PopularReviewSerializer
from .permissions import IsAdminUserOrReadOnly

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
    permission_classes = [permissions.IsAuthenticated]

class RequestUserImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RequestUserImage.objects.all()
    serializer_class = RequestUserImageSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PopularReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewSerializer
    permission_classes = [IsAdminUserOrReadOnly]
