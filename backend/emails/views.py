from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from rest_framework import serializers
import random
from users.models import CustomUser
from users.serializers import CustomUserSerializer

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

    try:
        template = get_template('code_for_reset_password.html')
    except django.template.exceptions.TemplateDoesNotExist:
        raise serializers.ValidationError("Html template was not found in the specified category")

    while step < 5:
        sendCodeForEmail()
        step += 1
        if step == 4:
            # Собираем полученный код
            code = "".join(map(str, arrayNumbers))

            # Рендеринг шаблона с контекстом
            html_message = template.render({'code': code})

            # Экземпляр письма
            try:
                mail_result = send_mail(
                    subject="Код подтверждения",
                    message="Код подтверждения",
                    html_message=html_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[userEmail],
                    fail_silently=False
                )
                print(mail_result)
            except:
                print("Код не отправлен на почту")

            # Отправляем код на фронт для валидации
            return Response(code, status=200)

@api_view(["GET"])
@permission_classes((AllowAny, ))
def check_email(request):
    email = request.GET.get("email")

    # В случае если такая почта имеется в БД отправить true
    # После отправки true, рекомендуется послать запрос на API по отправке кода на почту
    if CustomUser.objects.filter(email=email).exists():
        user = CustomUser.objects.filter(email=email)
        serializer = CustomUserSerializer(user, many=True, context={"request": request})
        object = { 'status': True, 'user': serializer.data }
        return Response(object, status=200)
    return Response(False, status=200)

