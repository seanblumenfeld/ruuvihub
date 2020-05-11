from decimal import Decimal

import factory

from web.ruuvitags.models import Event
from web.tests.factories.sensor import SensorFactory


class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = Event

    sensor = factory.SubFactory(SensorFactory)
    data_format = Event.DataFormat.FIVE
    humidity = Decimal('30.27')
    temperature = Decimal('26.24')
    pressure = Decimal('1013.49')
    acceleration = Decimal('990.1030249423542')
    acceleration_x = 56
    acceleration_y = -32
    acceleration_z = 988
    tx_power = 4
    battery = 3193
    movement_counter = 21
    measurement_sequence_number = 963
    mac = 'dummydata93d'
