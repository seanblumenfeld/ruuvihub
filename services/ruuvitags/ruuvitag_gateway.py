import json
import os

import environ
import requests
import ruuvitag_sensor.log
from rest_framework.utils import encoders
from ruuvitag_sensor.ruuvi import RuuviTagSensor

ruuvitag_sensor.log.enable_console()
logger = ruuvitag_sensor.log.log
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


def ignore_event(event):
    if event.get('measurement_sequence_number', 1) % 10 == 0:
        return False
    logger.info('Ignoring event')
    return True


def watch_sensor_events(data):
    mac, event = data
    logger.info(f'START: watch_sensor_events. MAC: {mac}. event: {event}')

    if ignore_event(event):
        return

    response = requests.post(
        url=f"{os.environ['PROTOCOL']}://{os.environ['HOST']}:{os.environ['PORT']}/api/events/",
        json=json.loads(encoders.JSONEncoder().encode(event)),
        headers={'Authorization': f"Bearer {os.environ['ACCESS_TOKEN']}"}
    )
    if response.status_code == 201:
        return response
    if response.status_code == 401:
        refresh_token()
        return watch_sensor_events(data)
    else:
        logger.error(response.text)


if __name__ == '__main__':
    environ.Env.read_env(env_file=ENV_FILE)
    obtain_tokens()
    RuuviTagSensor.get_datas(watch_sensor_events)
