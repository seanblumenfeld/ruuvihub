from django.utils.dateparse import parse_datetime
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from web.ruuvitags.models import Event, Sensor, Location
from web.ruuvitags.serializers import (
    EventSerializer, SensorSerializer, LocationSerializer,
    BroadcastSerializer
)


class BroadcastViewSet(mixins.CreateModelMixin, GenericViewSet):
    """API for a Ruuvitag broadcast data event."""
    queryset = Event.objects.all()
    serializer_class = BroadcastSerializer


class EventViewSet(ModelViewSet):
    """APIs for a Ruuvitag event."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ['location']

    def get_queryset(self):
        queryset = self.queryset
        created__gte = parse_datetime(self.request.query_params.get('created__gte', ''))
        if created__gte is not None:
            queryset = self.queryset.filter(created__gte=created__gte)
        return queryset


class LocationViewSet(ModelViewSet):
    """APIs for a Ruuvitag location object."""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filterset_fields = ['sensor']


class SensorViewSet(ModelViewSet):
    """APIs for a Ruuvitag sensor object."""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
