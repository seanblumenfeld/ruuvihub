import argparse
import json
from time import sleep

import requests
import structlog
from rest_framework.utils import encoders
from simple_ruuvitag import RuuviTagClient

logger = structlog.getLogger(__name__)


def post_sensor_event(mac, data):
    logger.debug(f'Received sensor data for {mac}')
    host = globals().get('HOST', 'localhost')
    port = globals().get('PORT', '8000')
    api_key = globals().get('API_KEY')
    response = requests.post(
        # TODO: parameterize? Move to settings?
        url=f'http://{host}:{port}/api/events/',
        json=json.loads(encoders.JSONEncoder().encode(data)),
        headers={'Authorization': f"Bearer {api_key}"}
    )
    logger.debug(f'Response: {response.status_code}')
    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default='8000')
    parser.add_argument('--api-key')
    xargs = parser.parse_args()

    HOST = xargs.host
    PORT = xargs.port
    API_KEY = xargs.api_key

    # TODO: get rid of this and run via supervisord or similar
    ruuvi_client = RuuviTagClient(callback=post_sensor_event)
    ruuvi_client.start()
    sleep(4)

    while True:
        logger.debug('RESTART')
        ruuvi_client.rescan()
        sleep(60*10)  # 10 minutes
