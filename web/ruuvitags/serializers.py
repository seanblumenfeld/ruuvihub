from rest_framework.serializers import ModelSerializer

from web.ruuvitags.models import Event, Sensor


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
