from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=56)
    projects = models.ManyToManyField("Project", blank=True)

    def __str__(self):
        return f"Категория - {self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Project(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=56)
    link_path = models.CharField(max_length=32)
    stack = models.TextField(blank=True)
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField("ProjectImage", blank=True)

    def __str__(self):
        return f"Проект - {self.name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class ProjectImage(models.Model):
    title = models.CharField(max_length=256)
    size = models.IntegerField(default=0, blank=True)
    image = models.ImageField(upload_to="images/%Y-%m-%d/")

    def __str__(self):
        return f"Изображение - {self.title}"

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проекта"
