import factory

from web.ruuvitags.models import Sensor
from web.tests.factories.base import BaseMetaFactory


class SensorFactory(BaseMetaFactory):
    class Meta:
        model = Sensor

    name = factory.Sequence(lambda n: f'name-{n}')
    mac_address = factory.Sequence(lambda n: f'DU:MM:YX:XX:XX:{n:02}')
    user = factory.SubFactory('web.tests.factories.user.UserFactory')
