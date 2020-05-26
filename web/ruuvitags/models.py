from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE
from django.utils.timezone import now

from web.core.abstract_models import BaseMetaModel
from web.settings.base import DECIMAL_PRECISION


def is_mac_address(value):
    raise Exception()


def is_mac(value):
    """Example - 'DU:MM:YD:AT:A9:3D'"""
    array = value.split(':')
    if len(array) != 6:
        raise ValidationError("Expected string of the form 'DU:MM:YD:AT:A9:3D'")


def get_sensor_name():
    return f'Sensor-{now()}'


class Sensor(BaseMetaModel):
    name = models.TextField(
        unique=True, default=get_sensor_name, help_text='A user editable identifier for a sensor.'
    )
    mac = models.CharField(
        unique=True, blank=False, null=False, max_length=17,
        validators=[MinLengthValidator(17), is_mac]
    )
    user = models.ForeignKey('users.User', on_delete=CASCADE)

    @property
    def owner(self):
        return self.user


class Event(BaseMetaModel):

    class DataFormat(models.IntegerChoices):
        """Reference: https://github.com/ruuvi/ruuvi-sensor-protocols """
        FIVE = 5

    sensor = models.ForeignKey(Sensor, related_name='events', on_delete=models.PROTECT)
    data_format = models.IntegerField(choices=DataFormat.choices, blank=False)
    humidity = models.DecimalField(blank=False, **DECIMAL_PRECISION)
    temperature = models.DecimalField(blank=False, **DECIMAL_PRECISION)
    pressure = models.DecimalField(blank=False, **DECIMAL_PRECISION)
    acceleration = models.DecimalField(blank=False, **DECIMAL_PRECISION)
    acceleration_x = models.IntegerField(blank=False)
    acceleration_y = models.IntegerField(blank=False)
    acceleration_z = models.IntegerField(blank=False)
    tx_power = models.IntegerField(blank=False)
    battery = models.IntegerField(blank=False)
    movement_counter = models.IntegerField(blank=False)
    measurement_sequence_number = models.IntegerField(blank=False)
    mac = models.CharField(max_length=17, validators=[is_mac])

    @property
    def owner(self):
        return self.sensor.user
