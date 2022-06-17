# Generated by Django 4.0.5 on 2022-06-17 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('numeroapp', '0004_numero_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numero_project',
            name='profile',
        ),
        migrations.AddField(
            model_name='numero_project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
