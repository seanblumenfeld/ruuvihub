from rest_framework.serializers import ModelSerializer

from web.ruuvitags.models import Events


class EventSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
