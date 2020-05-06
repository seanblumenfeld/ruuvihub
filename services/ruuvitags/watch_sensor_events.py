import json
from time import sleep

import requests
import structlog
from rest_framework.utils import encoders
from simple_ruuvitag import RuuviTagClient

logger = structlog.getLogger()

EVENTS_API = 'http://localhost:8000/events/'  # TODO: parameterize? Move to settings?
SENSOR_MACS = ['FE:F6:ED:CF:47:F3']


def save_sensor_event(mac, data):
    logger.info(f'Received sensor data for {mac}')
    response = requests.post(EVENTS_API, json={'data': json.dumps(data, cls=encoders.JSONEncoder)})
    logger.info(f'Response: {response.status_code}')


if __name__ == '__main__':
    ruuvi_client = RuuviTagClient(
        callback=save_sensor_event, mac_addresses=SENSOR_MACS
    )
    ruuvi_client.start()
    sleep(4)

    while True:
        logger.debug('RESTART')
        ruuvi_client.rescan()
        sleep(100)
