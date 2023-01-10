from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework_simplejwt.models import TokenUser


def requestImagePath(instance, filename):
    return "requests/request_{title}/images/{file}".format(title=instance.fk_request_user.name, file=filename)

def avatarImagePath(instance, filename):
    return "avatars/user_{username}/{file}".format(username=instance.username, file=filename)


class CustomTokenUser(TokenUser):
    def has_usable_password(self):
        return True

# Create your models here.

class CustomUser(AbstractUser):
    projects = models.ManyToManyField("backend_index.Project", blank=True, verbose_name="Проекты")
    telegram_username = models.CharField(
        max_length=32, blank=True, verbose_name="Телеграм username")
    reviews = models.ForeignKey("UserReview", blank=True, null=True, on_delete=models.CASCADE, verbose_name="Отзыв пользователя")
    avatar = models.ImageField(upload_to=avatarImagePath, blank=True, null=True, verbose_name="Аватарка")    

    def __str__(self):
        return self.username

# Заявки пользователей

class RequestUser(models.Model):
    fk_user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, blank=True,
                             verbose_name="Заголовок проекта")
    name = models.CharField(max_length=56, verbose_name="Имя проекта")
    stack = models.TextField(blank=True, verbose_name="Технологии")
    images = models.ManyToManyField(
        "RequestUserImage", blank=True, verbose_name="Изображения")

    def __str__(self):
        return f"Запрос пользователя - {self.name}, пользователь - {self.fk_user.username}"

    class Meta:
        verbose_name = "Запрос пользователя"
        verbose_name_plural = "Запросы пользователей"

# Изображения заявок

class RequestUserImage(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    fk_request_user = models.ForeignKey(RequestUser, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=requestImagePath, verbose_name="Изображение")

    def __str__(self):
        return f"Изображение - {self.title}"

    class Meta:
        verbose_name = "Изображение запроса пользователя"
        verbose_name_plural = "Изображения запросов пользователей"

# Пользовательские отзывы

class UserReview(models.Model):
    fk_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.TextField(verbose_name="Контент")
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Рейтинг")

    def __str__(self):
        return f"Отзыв пользователя - {self.fk_user.username}"

    class Meta:
        verbose_name = "Отзыв пользователя"
        verbose_name_plural = "Отзывы пользователей"

# Отзывы/популярные отзывы

class PopularReview(models.Model):
    fk_user_review = models.ForeignKey(UserReview, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Отзыв пользователя - {self.fk_user_review.fk_user.username}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    