# Generated by Django 4.1.3 on 2023-01-19 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_note_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='fk_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
