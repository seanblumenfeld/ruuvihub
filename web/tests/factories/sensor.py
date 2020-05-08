import factory

from web.ruuvitags.models import Sensor


class SensorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Sensor

    name = factory.Sequence(lambda n: f'name-{n}')
    mac_address = factory.Sequence(lambda n: f'DU:MM:YD:AT:A{n}:{n}{n}')
