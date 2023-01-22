from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser


@api_view(["GET"])
@permission_classes((AllowAny, ))
def getUsernameOnPhoneNumber(request):
    phone = request.GET.get("phone")
    password = request.GET.get("password")

    try:
        user = CustomUser.objects.get(phone=phone)
        if user.check_password(password):
            username = user.username
            return Response(username, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=400)
    except CustomUser.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=400)

