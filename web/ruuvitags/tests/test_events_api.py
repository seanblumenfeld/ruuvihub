from rest_framework.reverse import reverse

from web.ruuvitags.models import Event, Sensor, mac_to_mac_address
from web.ruuvitags.tests.helpers import DATA_FORMAT_5_EXAMPLE
from web.tests.factories.event import EventFactory
from web.tests.factories.sensor import SensorFactory
from web.tests.helpers import BaseTestCase


class EventCreateTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = reverse('events-list')

    def test_can_create_event(self):
        response = self.client.post(path=self.path, data=DATA_FORMAT_5_EXAMPLE)
        self.assertResponse201(response)

    def test_400_when_no_payload_provided(self):
        response = self.client.post(path=self.path)
        self.assertResponse400(response)
        self.assertEqual(response.data['data_format'][0].code, 'required')
        self.assertEqual(response.data['humidity'][0].code, 'required')
        self.assertEqual(response.data['temperature'][0].code, 'required')
        self.assertEqual(response.data['pressure'][0].code, 'required')
        self.assertEqual(response.data['acceleration'][0].code, 'required')
        self.assertEqual(response.data['acceleration_x'][0].code, 'required')
        self.assertEqual(response.data['acceleration_y'][0].code, 'required')
        self.assertEqual(response.data['acceleration_z'][0].code, 'required')
        self.assertEqual(response.data['tx_power'][0].code, 'required')
        self.assertEqual(response.data['battery'][0].code, 'required')
        self.assertEqual(response.data['movement_counter'][0].code, 'required')
        self.assertEqual(response.data['measurement_sequence_number'][0].code, 'required')
        self.assertEqual(response.data['mac'][0].code, 'required')

    def test_event_from_new_sensor_creates_sensor_db_object(self):
        response = self.client.post(path=self.path, data=DATA_FORMAT_5_EXAMPLE)
        self.assertResponse201(response)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Sensor.objects.count(), 1)

    def test_event_from_known_sensor(self):
        mac_address = mac_to_mac_address(DATA_FORMAT_5_EXAMPLE['mac'])
        sensor = SensorFactory(mac_address=mac_address)
        response = self.client.post(path=self.path, data=DATA_FORMAT_5_EXAMPLE)
        self.assertResponse201(response)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Sensor.objects.count(), 1)
        self.assertEqual(Event.objects.get(id=response.data['id']).sensor, sensor)


class EventDetailTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.event = EventFactory()
        cls.path = reverse('events-detail', args=(cls.event.id,))

    def test_can_get_event(self):
        response = self.client.get(path=self.path)
        self.assertResponse200(
            response, data_contains={'id': self.event.id_str}
        )
