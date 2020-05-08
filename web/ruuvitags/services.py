import json

import structlog
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.utils import encoders
from ruuvitag_sensor.ruuvi import RuuviTagSensor

from web.ruuvitags.models import Sensor
from web.ruuvitags.serializers import SensorSerializer, EventSerializer

logger = structlog.getLogger(settings.APP_LOGGER)


class RuuvitagsServiceException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Cannot save ruuvitag.')
    default_code = 'error'


def find_and_save_sensors(sensor_adapter: RuuviTagSensor = RuuviTagSensor):
    ruuvitags = sensor_adapter.find_ruuvitags()

    new_sensors = []
    for mac_address, sensor_data in ruuvitags.items():
        try:
            Sensor.objects.get(mac_address=mac_address)
        except Sensor.DoesNotExist:
            new_sensors.append({
                'name': mac_address,
                'mac_address': mac_address,
                'data': json.dumps(sensor_data),
            })

    serializer = SensorSerializer(data=new_sensors, many=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.validated_data


def save_sensor_event(mac, data):
    logger.info(f'Received sensor data for {mac}')
    serializer = EventSerializer(data={'data': json.dumps(data, cls=encoders.JSONEncoder)})
    serializer.is_valid(raise_exception=True)
    serializer.save()
