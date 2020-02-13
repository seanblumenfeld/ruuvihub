from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView

from web.ruuvitags.models import Events
from web.ruuvitags.serializers import EventSerializer


class PaymentsServiceException(APIException):
    status_code = 400
    default_detail = 'External Payment Service Error.'
    default_code = 'external_payment_service_error'


class CreateEventAPI(CreateAPIView):
    """Api to process a payment charge."""
    name = 'temperature-load'
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = []  # TODO
