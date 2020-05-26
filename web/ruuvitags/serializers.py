from django.db import transaction
from rest_framework.serializers import ModelSerializer

from web.ruuvitags.models import Event, Sensor


class SensorSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ['user']


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        depth = 1

    @transaction.atomic()
    def create(self, validated_data):
        # Create sensor if required
        sensor = Sensor.objects.get_or_create(
            mac=validated_data['mac'],
            user=self.context['request'].user
        )[0]
        # Create event
        validated_data['sensor'] = sensor
        return super().create(validated_data)
