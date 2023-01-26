from django.db import models
from users.models import CustomUser


def projectImagePath(instance, filename):
    return "projects/{title}/images/{file}".format(title=instance.fk_project.link_path, file=filename)

# Create your models here.

# Категории
class Category(models.Model):
    title = models.CharField(max_length=56, verbose_name="Категория")
    projects = models.ManyToManyField(
        "Project", blank=True, verbose_name="Проекты")
    prefix = models.SlugField(max_length=42, verbose_name="Префикс")

    def __str__(self):
        return f"Категория - {self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

# Проекты которые были созданы!!!
# По возможности можно добавить пользователя, заявка которого была принята - проект создан.
class Project(models.Model):
    fk_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=256, verbose_name="Заголовок проекта")
    data_complete = models.CharField(max_length=28, verbose_name="Дата завершения проекта")
    name = models.CharField(max_length=56, verbose_name="Имя проекта")
    link_path = models.SlugField(max_length=32, verbose_name="Api проекта")
    stacks = models.ManyToManyField("Stack", blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="Описание проекта")
    website = models.URLField(blank=True, verbose_name="WebSite")
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField("ProjectImage", blank=True, verbose_name="Изображения")
    status = models.BooleanField(default=False, blank=True, verbose_name="Статус принятия")
    complete = models.BooleanField(default=False, blank=True, verbose_name="Проект завершен")

    def __str__(self):
        return f"Проект - {self.name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

# Технологии
class Stack(models.Model):
    stack = models.CharField(max_length=32, verbose_name="Технология")
    color = models.CharField(max_length=12, verbose_name="Цвет")
    description = models.TextField(verbose_name="Описание технологии")

    def __str__(self):
        return f"Технология - {self.stack}"

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"
        
# Изображения проектов
class ProjectImage(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    fk_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=projectImagePath, verbose_name="Изображение")

    def __str__(self):
        return f"Изображение - {self.title}"

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проекта"
