import factory

from web.ruuvitags.models import Location
from web.tests.factories.base import BaseMetaFactory
from web.tests.factories.sensor import SensorFactory


class LocationFactory(BaseMetaFactory):
    class Meta:
        model = Location

    name = factory.Sequence(lambda n: f'name-{n}')
    sensor = factory.SubFactory(SensorFactory)
