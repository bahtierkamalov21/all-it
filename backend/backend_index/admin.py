from django.contrib import admin
from .models import Category, Project, ProjectImage, Stack

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Stack)
