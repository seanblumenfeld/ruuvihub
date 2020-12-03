from rest_framework.reverse import reverse

from web.ruuvitags.models import Event, Sensor, Location
from web.ruuvitags.tests.helpers import DATA_FORMAT_5_EXAMPLE
from web.tests.factories.event import EventFactory
from web.tests.factories.sensor import SensorFactory
from web.tests.factories.user import UserFactory
from web.tests.helpers import BaseTestCase, get_api_token


class BroadcastTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = reverse('broadcasts-list')

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        token = get_api_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_broadcast(self):
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

    def test_broadcast_from_new_sensor_creates_all_ruuvitag_objects(self):
        response = self.client.post(path=self.path, data=DATA_FORMAT_5_EXAMPLE)
        self.assertResponse201(response)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Location.objects.count(), 1)
        self.assertEqual(Sensor.objects.count(), 1)

    def test_broadcast_from_known_sensor(self):
        sensor = SensorFactory(mac=DATA_FORMAT_5_EXAMPLE['mac'], user=self.user)
        response = self.client.post(path=self.path, data=DATA_FORMAT_5_EXAMPLE)
        self.assertResponse201(response)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Sensor.objects.count(), 1)
        self.assertEqual(Event.objects.get(id=response.data['id']).location.sensor, sensor)

    def test_cant_list_events(self):
        EventFactory.create_batch(size=4)
        response = self.client.get(path=reverse('broadcasts-list'))
        self.assertResponse(response, 405)
