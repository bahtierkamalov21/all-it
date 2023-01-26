from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework_simplejwt.models import TokenUser


def avatarImagePath(instance, filename):
    return "avatars/user_{username}/{file}".format(username=instance.username, file=filename)

# Create your models here.
class CustomUser(AbstractUser):
    projects = models.ManyToManyField("backend_index.Project", blank=True, verbose_name="Проекты")
    telegram_username = models.CharField(
        max_length=32, blank=True, verbose_name="Телеграм username")
    phone = models.CharField(max_length=28)
    review = models.ForeignKey("UserReview", blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Отзыв пользователя")
    avatar = models.ImageField(upload_to=avatarImagePath, blank=True, null=True, verbose_name="Аватарка")   

    def __str__(self):
        return self.username

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
        verbose_name = "Популярный отзыв"
        verbose_name_plural = "Популярные отзывы"
    