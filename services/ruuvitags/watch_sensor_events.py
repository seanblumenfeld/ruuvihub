import os

import environ
import json
from time import sleep

import requests
import structlog
from rest_framework.utils import encoders
from simple_ruuvitag import RuuviTagClient

logger = structlog.getLogger(__name__)
ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')


def obtain_tokens():
    logger.info('START: obtain_tokens')
    response = requests.post(
        url=f"{os.getenv('PROTOCOL')}://{os.getenv('HOST')}:{os.getenv('PORT')}/api/token/obtain/",
        json={
            'username': os.environ['USERNAME'],
            'password': os.environ['PASSWORD'],
        },
    )
    response.raise_for_status()
    tokens = response.json()
    os.environ['REFRESH_TOKEN'] = tokens['refresh']
    os.environ['ACCESS_TOKEN'] = tokens['access']


def refresh_token():
    logger.info('START: refresh_tokens')
    if not os.environ.get('REFRESH_TOKEN'):
        obtain_tokens()
    response = requests.post(
        url=f"{os.getenv('PROTOCOL')}://{os.getenv('HOST')}:{os.getenv('PORT')}/api/token/refresh/",
        json={
            'refresh': os.environ['REFRESH_TOKEN'],
        },
    )
    tokens = response.json()
    os.environ['REFRESH_TOKEN'] = tokens['refresh']
    os.environ['ACCESS_TOKEN'] = tokens['access']
    response.raise_for_status()


def watch_sensor_events(mac, data):
    logger.info(f'START: watch_sensor_events. MAC: {mac}')
    response = requests.post(
        url=f"{os.environ['PROTOCOL']}://{os.environ['HOST']}:{os.environ['PORT']}/api/events/",
        json=json.loads(encoders.JSONEncoder().encode(data)),
        headers={'Authorization': f"Bearer {os.environ['ACCESS_TOKEN']}"}
    )
    if response.status_code == 201:
        return response
    if response.status_code == 401:
        refresh_token()
        return watch_sensor_events(mac, data)
    else:
        logger.error(response.json())


if __name__ == '__main__':
    environ.Env.read_env(env_file=ENV_FILE)

    obtain_tokens()
    # TODO: get rid of this and run via supervisord or similar
    ruuvi_client = RuuviTagClient(callback=watch_sensor_events)
    ruuvi_client.start()
    sleep(4)

    while True:
        logger.debug('RESTART')
        ruuvi_client.rescan()
        sleep(60*10)  # 10 minutes
