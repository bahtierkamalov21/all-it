# Generated by Django 4.1.3 on 2022-12-18 12:00

import backend_index.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=56, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок проекта')),
                ('name', models.CharField(max_length=56, verbose_name='Имя проекта')),
                ('link_path', models.SlugField(max_length=32, verbose_name='Api проекта')),
                ('stack', models.TextField(blank=True, verbose_name='Технологии')),
                ('status', models.BooleanField(blank=True, default=False, verbose_name='Статус принятия')),
                ('complete', models.BooleanField(blank=True, default=False, verbose_name='Проект завершен')),
                ('fk_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_index.category')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('image', models.ImageField(upload_to=backend_index.models.projectImagePath, verbose_name='Изображение')),
                ('fk_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_index.project')),
            ],
            options={
                'verbose_name': 'Изображение проекта',
                'verbose_name_plural': 'Изображения проекта',
            },
        ),
    ]
