# Generated by Django 4.1.3 on 2022-12-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_index', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='prefix',
            field=models.SlugField(default='0', max_length=42, verbose_name='Префикс'),
            preserve_default=False,
        ),
    ]
