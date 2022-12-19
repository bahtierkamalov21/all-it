# Generated by Django 4.1.3 on 2022-12-18 12:00

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('backend_index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telegram_username', models.CharField(blank=True, max_length=32, null=True, verbose_name='Телеграм username')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=users.models.avatarImagePath, verbose_name='Аватарка')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('projects', models.ManyToManyField(blank=True, to='backend_index.project', verbose_name='Проекты')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RequestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Заголовок проекта')),
                ('name', models.CharField(max_length=56, verbose_name='Имя проекта')),
                ('stack', models.TextField(blank=True, verbose_name='Технологии')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Запрос пользователя',
                'verbose_name_plural': 'Запросы пользователей',
            },
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(verbose_name='Контент')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв пользователя',
                'verbose_name_plural': 'Отзывы пользователей',
            },
        ),
        migrations.CreateModel(
            name='RequestUserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('image', models.ImageField(upload_to=users.models.requestImagePath, verbose_name='Изображение')),
                ('fk_request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.requestuser')),
            ],
            options={
                'verbose_name': 'Изображение запроса пользователя',
                'verbose_name_plural': 'Изображения запросов пользователей',
            },
        ),
        migrations.AddField(
            model_name='requestuser',
            name='images',
            field=models.ManyToManyField(blank=True, to='users.requestuserimage', verbose_name='Изображения'),
        ),
        migrations.CreateModel(
            name='PopularReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_user_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userreview')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='requests',
            field=models.ManyToManyField(blank=True, to='users.requestuser', verbose_name='Заявки пользователя'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reviews',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.userreview', verbose_name='Отзыв пользователя'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]