# Generated by Django 3.0.6 on 2020-05-08 11:18

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import uuid
import web.ruuvitags.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(validators=[web.ruuvitags.models.is_json_deserializable])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField(help_text='A user editable identifier for a sensor.', unique=True)),
                ('mac_address', models.CharField(max_length=17, unique=True, validators=[django.core.validators.MinLengthValidator(17), web.ruuvitags.models.is_mac_address])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
