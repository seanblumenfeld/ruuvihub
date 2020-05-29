from django.db import transaction
from rest_framework.serializers import ModelSerializer

from web.ruuvitags.models import Event, Sensor, Location


class SensorSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ['user']


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class BroadcastSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['location']

    @transaction.atomic()
    def create(self, validated_data):
        # Create sensor and location if required
        sensor = Sensor.objects.get_or_create(
            mac=validated_data['mac'],
            user=self.context['request'].user
        )[0]
        location = Location.get_latest_for_sensor_or_create(sensor=sensor)
        # Create event
        validated_data['location'] = location
        return super().create(validated_data)
