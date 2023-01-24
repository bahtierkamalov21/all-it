# Generated by Django 4.1.3 on 2023-01-24 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend_index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='fk_user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(blank=True, to='backend_index.projectimage', verbose_name='Изображения'),
        ),
        migrations.AddField(
            model_name='project',
            name='stacks',
            field=models.ManyToManyField(blank=True, null=True, to='backend_index.stack'),
        ),
        migrations.AddField(
            model_name='category',
            name='projects',
            field=models.ManyToManyField(blank=True, to='backend_index.project', verbose_name='Проекты'),
        ),
    ]