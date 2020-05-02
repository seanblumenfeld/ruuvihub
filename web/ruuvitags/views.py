from rest_framework.viewsets import ModelViewSet

from web.ruuvitags.models import Event, Sensor
from web.ruuvitags.serializers import EventSerializer, SensorSerializer


class EventViewSet(ModelViewSet):
    """APIs for a Ruuvitag sensor's broadcast data event."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SensorViewSet(ModelViewSet):
    """APIs for a Ruuvitag sensor object."""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
