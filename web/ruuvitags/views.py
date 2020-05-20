from django.utils.dateparse import parse_datetime
from rest_framework.viewsets import ModelViewSet

from web.ruuvitags.models import Event, Sensor
from web.ruuvitags.serializers import EventSerializer, SensorSerializer


class EventViewSet(ModelViewSet):
    """APIs for a Ruuvitag sensor's broadcast data event."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ['sensor']  # Generic filtering using DEFAULT_FILTER_BACKENDS

    def get_queryset(self):
        queryset = self.queryset
        created__gte = parse_datetime(self.request.query_params.get('created__gte', ''))
        if created__gte is not None:
            queryset = self.queryset.filter(created__gte=created__gte)
        return queryset


class SensorViewSet(ModelViewSet):
    """APIs for a Ruuvitag sensor object."""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
