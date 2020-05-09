# Generated by Django 3.0.6 on 2020-05-09 10:49

from django.db import migrations, models
import web.ruuvitags.models


class Migration(migrations.Migration):

    dependencies = [
        ('ruuvitags', '0002_event_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.TextField(default=web.ruuvitags.models.get_sensor_name, help_text='A user editable identifier for a sensor.', unique=True),
        ),
    ]
