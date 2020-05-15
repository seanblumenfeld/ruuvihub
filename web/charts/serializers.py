from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from web.ruuvitags.models import Event
from web.settings.base import DECIMAL_PRECISION


class TemperatureChartDataSerializer(ModelSerializer):
    x = serializers.DateTimeField(read_only=True, source='created')
    y = serializers.DecimalField(**DECIMAL_PRECISION, read_only=True, source='temperature')

    class Meta:
        model = Event
        fields = ('x', 'y')
