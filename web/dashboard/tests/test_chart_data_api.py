from collections import OrderedDict

from rest_framework.reverse import reverse

from web.tests.factories.event import EventFactory
from web.tests.helpers import BaseTestCase


class EventDetailTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.events = EventFactory.create_batch(size=10)
        cls.path = reverse('chart-data-temp-view')

    def test_can_get_data(self):
        response = self.client.get(path=self.path)
        dt_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        self.assertResponse200(
            response,
            data=[
                OrderedDict(x=e.created.strftime(dt_format), y=f'{e.temperature:.15f}')
                for e in self.events
            ]
        )
