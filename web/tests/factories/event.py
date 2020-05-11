import factory

from web.ruuvitags.models import Event
from web.ruuvitags.tests.helpers import DATA_FORMAT_5_EXAMPLE
from web.tests.factories.sensor import SensorFactory


class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = Event

    data = DATA_FORMAT_5_EXAMPLE
    sensor = factory.SubFactory(SensorFactory)
