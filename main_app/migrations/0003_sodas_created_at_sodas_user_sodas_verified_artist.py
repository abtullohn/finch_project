# Generated by Django 4.1.2 on 2022-10-06 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_rename_soda_sodas'),
    ]

    operations = [
        migrations.AddField(
            model_name='sodas',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sodas',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sodas',
            name='verified_artist',
            field=models.BooleanField(default=False),
        ),
    ]
