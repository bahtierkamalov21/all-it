from urllib import response
from rest_framework import viewsets, permissions
from .models import CustomUser, RequestUser, RequestUserImage, UserReview, PopularReview
from .serializers import CustomUserSerializer, RequestUserSerializer, RequestUserImageSerializer, UserReviewSerializer, PopularReviewSerializer
from .permissions import IsAdminUserOrReadOnly
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.conf import settings

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

def reset_password_and_email_send_code(request):
    step = 0
    arrayNumbers = []
    code = ""

    def sendCodeForEmail():
        arrayNumbers.append(int(random.randrange(0, 10)))

    while step < 5:
        sendCodeForEmail()
        step += 1
        if step == 4:
            code = "".join(map(str, arrayNumbers))
            send_mail(
                subject=code,
                message="Код доступа",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['bakhtiyorkamalov22@gmail.com'],
                fail_silently=False
            )
            return HttpResponse(code)
