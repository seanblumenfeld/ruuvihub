import json
import logging

from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.utils import encoders
from ruuvitag_sensor.ruuvi import RuuviTagSensor

from web.ruuvitags.models import Sensors, Events
from web.ruuvitags.serializers import SensorSerializer


class RuuvitagsServiceException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Cannot save ruuvitag.')
    default_code = 'error'


def find_and_save_sensors(sensor_adapter: RuuviTagSensor = RuuviTagSensor):
    ruuvitags = sensor_adapter.find_ruuvitags()

    new_sensors = []
    for sensor_id, sensor_data in ruuvitags.items():
        try:
            Sensors.objects.get(sensor_id=sensor_id)
        except Sensors.DoesNotExist:
            new_sensors.append({
                'name': sensor_id,
                'sensor_id': sensor_id,
                'data': json.dumps(sensor_data),
            })

    serializer = SensorSerializer(data=new_sensors, many=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.validated_data


def save_sensor_event(mac, data):
    logging.info(f'Received sensor data for {mac}')
    if data:
        Events.objects.create(data=json.dumps(data, cls=encoders.JSONEncoder))
