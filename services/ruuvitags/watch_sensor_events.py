import json
import os
from time import sleep

import environ
import requests
import structlog
from rest_framework.utils import encoders
from simple_ruuvitag import RuuviTagClient

logger = structlog.getLogger(__name__)

# TODO: implement .test.env for tests?
env_file = os.path.join('environments', '.dev.env')
environ.Env.read_env(env_file=env_file)

# TODO: parameterize? Move to settings?
BASE_URI = f"http://{os.getenv('DJANGO_HOST')}:{os.getenv('DJANGO_PORT')}/"
EVENT_API = f'{BASE_URI}events/'
SENSOR_API = f'{BASE_URI}sensors/'


def post_sensor_event(mac, data):
    logger.debug(f'Received sensor data for {mac}')
    response = requests.post(
        EVENT_API,
        json=json.loads(encoders.JSONEncoder().encode(data)),
    )
    logger.debug(f'Response: {response.status_code}')


if __name__ == '__main__':
    # TODO: get rid of this and run via supervisord or similar
    ruuvi_client = RuuviTagClient(callback=post_sensor_event)
    ruuvi_client.start()
    sleep(4)

    while True:
        logger.debug('RESTART')
        ruuvi_client.rescan()
        sleep(60*10)  # 10 minutes
