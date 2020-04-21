from django.conf import settings
from huey import crontab
from huey.contrib import djhuey
from simple_ruuvitag import RuuviTagClient

from web.ruuvitags import services


@djhuey.db_periodic_task(crontab(minute='*'))
def save_sensor_event():
    ruuvi_client = RuuviTagClient(
        callback=services.save_sensor_event,
        mac_addresses=settings.SENSOR_MACS
    )
    ruuvi_client.start()
