import factory

from web.ruuvitags.models import Sensor


class SensorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Sensor

    name = factory.Sequence(lambda n: f'name-{n}')
    sensor_id = factory.Sequence(lambda n: f'DU:MM:YD:AT:A{n}:{n}{n}')
    data = {}
