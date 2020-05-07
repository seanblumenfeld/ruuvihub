import json
from time import sleep

import requests
import structlog
from rest_framework.utils import encoders
from simple_ruuvitag import RuuviTagClient

logger = structlog.getLogger()

# TODO: parameterize? Move to settings?
EVENT_API = 'http://localhost:8000/events/'
SENSOR_API = 'http://localhost:8000/sensors/'


def save_sensor_event(mac, data):
    logger.debug(f'Received sensor data for {mac}')
    response = requests.post(EVENT_API, json={'data': json.dumps(data, cls=encoders.JSONEncoder)})
    logger.debug(f'Response: {response.status_code}')


def get_sensor_mac_addresses():
    response = requests.get(SENSOR_API)
    logger.debug(f'Response: {response.status_code}')
    return [s['sensor_id'] for s in response.json()]


if __name__ == '__main__':
    # TODO: get rid of this and run via supervisord or similar
    mac_addresses = get_sensor_mac_addresses()
    ruuvi_client = RuuviTagClient(
        callback=save_sensor_event, mac_addresses=mac_addresses
    )
    ruuvi_client.start()
    sleep(4)

    while True:
        logger.debug('RESTART')
        ruuvi_client.rescan()
        sleep(60*10)  # 10 minutes
