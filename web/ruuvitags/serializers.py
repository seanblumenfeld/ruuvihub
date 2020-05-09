from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from web.ruuvitags.models import Event, Sensor, is_mac_address


class SensorSerializer(ModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'


class EventSerializer(ModelSerializer):
    mac_address = serializers.CharField(required=True, validators=[is_mac_address], write_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        mac_address = validated_data.pop('mac_address')
        sensor = Sensor.objects.get_or_create(mac_address=mac_address)[0]
        validated_data['sensor'] = sensor
        return super().create(validated_data)
