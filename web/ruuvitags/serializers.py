from rest_framework.serializers import ModelSerializer

from web.ruuvitags.models import Events, Sensors


class EventSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'
