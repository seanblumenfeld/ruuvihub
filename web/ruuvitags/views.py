from rest_framework.viewsets import ModelViewSet

from web.ruuvitags.models import Events, Sensors
from web.ruuvitags.serializers import EventSerializer, SensorSerializer


class EventViewSet(ModelViewSet):
    """API to save a Ruuvitag sensor's broadcast data."""
    url_prefix = r'events'
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class SensorViewSet(ModelViewSet):
    url_prefix = r'sensors'
    queryset = Sensors.objects.all()
    serializer_class = SensorSerializer
