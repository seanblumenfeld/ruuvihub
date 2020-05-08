import json

from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from web.core.abstract_models import BaseMetaModel


def is_json_deserializable(value):
    try:
        json.loads(json.dumps(value))
    except json.decoder.JSONDecodeError as e:
        raise ValidationError(e.args)


def is_mac_address(value):
    """Example - 'DU:MM:YD:AT:A9:3D'"""
    array = value.split(':')
    if len(array) != 6:
        raise ValidationError("Expected string of the form 'DU:MM:YD:AT:A9:3D'")


class Event(BaseMetaModel):
    data = JSONField(blank=False, null=False, validators=[is_json_deserializable])


class Sensor(BaseMetaModel):
    name = models.TextField(
        unique=True, blank=False, null=False, help_text='A user editable identifier for a sensor.'
    )
    mac_address = models.CharField(
        unique=True, blank=False, null=False, max_length=17,
        validators=[MinLengthValidator(17), is_mac_address]
    )
