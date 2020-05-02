import factory

from web.ruuvitags.models import Event


class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = Event

    data = {}
