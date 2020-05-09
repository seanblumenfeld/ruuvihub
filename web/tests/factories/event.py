import factory

from web.ruuvitags.models import Event
from web.tests.factories.sensor import SensorFactory


class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = Event

    data = {}
    sensor = factory.SubFactory(SensorFactory)
