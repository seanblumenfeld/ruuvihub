from web.ruuvitags.models import StructuredEvent
from web.ruuvitags.tasks import create_structured_event
from web.tests.factories.event import EventFactory
from web.tests.helpers import BaseTestCase


class StructuredEventTests(BaseTestCase):

    def test_create_structured_event(self):
        event = EventFactory()
        result = create_structured_event(event)
        structured_event = StructuredEvent.objects.get(event_id=event.id)
        self.assertEqual(result.get(), structured_event)
        self.assertEqual(event.data['data_format'], structured_event.data_format)
