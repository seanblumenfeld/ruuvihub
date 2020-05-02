import json
from time import sleep

import requests
import structlog
from rest_framework.utils import encoders
from simple_ruuvitag import RuuviTagClient

logger = structlog.getLogger()

events_api = 'http://localhost:8000/events/'  # TODO: parameterize? Move to settings?
SENSOR_MACS = ['FE:F6:ED:CF:47:F3']


def save_sensor_event(mac, data):
    logger.debug(f'Received sensor data for {mac}')
    response = requests.post(events_api, json={'data': json.dumps(data, cls=encoders.JSONEncoder)})
    logger.debug(f'Response: {response.status_code}')


if __name__ == '__main__':
    ruuvi_client = RuuviTagClient(
        callback=save_sensor_event, mac_addresses=SENSOR_MACS
    )
    ruuvi_client.start()
    sleep(4)
    logger.debug('RESTART')
    ruuvi_client.rescan()
    sleep(1000)
