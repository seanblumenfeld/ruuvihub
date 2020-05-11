from rest_framework.reverse import reverse

from web.ruuvitags.models import Event, Sensor
from web.tests.factories.event import EventFactory
from web.tests.factories.sensor import SensorFactory
from web.tests.helpers import BaseTestCase


class EventCreateTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = reverse('events-list')

    def setUp(self):
        super().setUp()
        self.event_data = {
            'data': {},
            'mac_address': 'DU:MM:YD:AT:AX:XX'
        }

    def test_can_create_event(self):
        response = self.client.post(path=self.path, data=self.event_data)
        self.assertResponse201(response, data_contains={'data': {}})

    def test_400_when_no_data_provided(self):
        response = self.client.post(path=self.path)
        self.assertResponse400(response)
        self.assertEqual(response.data['data'][0].code, 'required')

    def test_event_from_new_sensor_creates_sensor_db_object(self):
        response = self.client.post(path=self.path, data=self.event_data)
        self.assertResponse201(response)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Sensor.objects.count(), 1)

    def test_event_from_known_sensor(self):
        SensorFactory(mac_address=self.event_data['mac_address'])
        response = self.client.post(path=self.path, data=self.event_data)
        self.assertResponse201(response)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Sensor.objects.count(), 1)


class EventDetailTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.event = EventFactory()
        cls.path = reverse('events-detail', args=(cls.event.id,))

    def test_can_get_event(self):
        response = self.client.get(path=self.path)
        self.assertResponse200(
            response, data_contains={'id': self.event.id_str, 'data': self.event.data}
        )
