import argparse
import json
import os
from time import sleep

import environ
import requests
import ruuvitag_sensor.log
from rest_framework.utils import encoders
from ruuvitag_sensor.ruuvi import RuuviTagSensor
from simple_ruuvitag import RuuviTagClient

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
    if event.get('measurement_sequence_number', 1) % int(os.environ['IGNORE_INTERVAL']) == 0:
        return False
    logger.info('Ignoring event')
    return True


def _watch_sensor_events(mac, event):
    logger.info(f'START: watch_sensor_events. MAC: {mac}. event: {event}')

    if ignore_event(event):
        return

    event['mac'] = mac
    response = requests.post(
        url=f"{os.environ['PROTOCOL']}://{os.environ['HOST']}:{os.environ['PORT']}"
            "/api/ruuvitags/broadcasts/",
        json=json.loads(encoders.JSONEncoder().encode(event)),
        headers={'Authorization': f"Bearer {os.environ['ACCESS_TOKEN']}"}
    )
    if response.status_code == 201:
        return response
    if response.status_code == 401:
        refresh_token()
        return _watch_sensor_events(mac, event)
    else:
        logger.error(response.text)


def simple_ruuvitag_watch_sensor_events(mac, event):
    return _watch_sensor_events(mac, event)


def ruuvitag_sensor_watch_sensor_events(data):
    mac, event = data
    return _watch_sensor_events(mac, event)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--use-simple-ruuvitag', action='store_true', default=False)
    parser.add_argument('--ignore-interval', type=int, default=10)
    xargs = parser.parse_args()

    os.environ['IGNORE_INTERVAL'] = str(xargs.ignore_interval)
    environ.Env.read_env(env_file=ENV_FILE)
    obtain_tokens()

    if xargs.use_simple_ruuvitag:
        ruuvi_client = RuuviTagClient(callback=simple_ruuvitag_watch_sensor_events)
        ruuvi_client.start()
        sleep(4)
        while True:
            ruuvi_client.rescan()
            sleep(60 * 10)  # 10 minutes
    else:
        RuuviTagSensor.get_data(ruuvitag_sensor_watch_sensor_events)
