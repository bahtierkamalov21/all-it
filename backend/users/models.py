from django.db import models
from django.contrib.auth.models import AbstractUser


def requestImagePath(instance, filename):
    return "request_{title}/images/{file}".format(title=instance.fk_request_user.name, file=filename)

# Create your models here.
class CustomUser(AbstractUser):
	requests = models.ManyToManyField(
	    "RequestUser", blank=True, verbose_name="Запросы")
	telegram_username = models.CharField(
	    blank=True, max_length=32, verbose_name="Телеграм username")

	def __str__(self):
		return self.username

class RequestUser(models.Model):
    fk_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=256, blank=True, verbose_name="Заголовок проекта")
    name = models.CharField(max_length=56, verbose_name="Имя проекта")
    stack = models.TextField(blank=True, verbose_name="Технологии")
    images = models.ManyToManyField("RequestUserImage", blank=True, verbose_name="Изображения")

    def __str__(self):
        return f"Запрос пользователя - {self.name}, пользователь - {self.fk_user.username}"
    
    class Meta:
        verbose_name = "Запрос пользователя"
        verbose_name_plural = "Запросы пользователей"
        
# Изображения запросов

class RequestUserImage(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    fk_request_user = models.ForeignKey(RequestUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=requestImagePath, verbose_name="Изображение")

    def __str__(self):
        return f"Изображение - {self.title}"

    class Meta:
        verbose_name = "Изображение запроса пользователя"
        verbose_name_plural = "Изображения запросов пользователей"
