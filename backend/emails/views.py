from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.
@api_view(["POST"])
@permission_classes((AllowAny, ))
def reset_password_and_email_send_code(request):
    step = 0
    arrayNumbers = []
    code = ""
    userEmail = request.GET.get("email")

    def sendCodeForEmail():
        arrayNumbers.append(int(random.randrange(0, 10)))

    while step < 5:
        sendCodeForEmail()
        step += 1
        if step == 4:
            code = "".join(map(str, arrayNumbers))
            send_mail(
                subject="Код подтверждения",
                message=f"Код подтверждения: {code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[userEmail],
                fail_silently=True
            )
            return Response(code, status=200)
