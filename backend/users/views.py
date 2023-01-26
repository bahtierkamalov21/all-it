from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser, UserReview, PopularReview
from .serializers import CustomUserSerializer, UserReviewSerializer, PopularReviewSerializer
from .permissions import IsAdminUserOrReadOnly
from django.conf import settings
import jwt

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class UserReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.AllowAny]

class PopularReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewSerializer
    permission_classes = [IsAdminUserOrReadOnly]

@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def decoded_tokens(request):
    token = request.headers["Authorization"].replace("Bearer ", "")
    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    return Response(decoded, status=200)
