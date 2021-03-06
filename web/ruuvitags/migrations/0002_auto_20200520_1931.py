# Generated by Django 3.0.6 on 2020-05-20 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ruuvitags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='ruuvitags.Sensor'),
        ),
    ]
