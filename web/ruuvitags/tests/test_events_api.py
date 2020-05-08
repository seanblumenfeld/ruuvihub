from rest_framework.reverse import reverse

from web.tests.factories.event import EventFactory
from web.tests.helpers import BaseTestCase


class EventCreateTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = reverse('events-list')

    def test_can_create_event(self):
        response = self.client.post(path=self.path, data={'data': {}})
        self.assertResponse201(response)

    def test_400_when_no_data_provided(self):
        response = self.client.post(path=self.path)
        self.assertResponse400(response)
        self.assertEqual(response.data['data'][0].code, 'required')


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


class SensorViewSetTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.path = reverse('sensors-list')

    def test_can_create_sensor(self):
        name = 'new-sensor'
        response = self.client.post(
            path=self.path,
            data={'name': name, 'data': '{}', 'sensor_id': 'DU:MM:YD:AT:A9:3D'},
        )
        self.assertResponse201(response)
        self.assertEqual(response.data['name'], name)
        self.assertEqual(response.data['data'], '{}')

    def test_400_when_params_not_provided(self):
        response = self.client.post(path=self.path)
        self.assertResponse400(response)
        self.assertEqual(response.data['name'][0].code, 'required')
        self.assertEqual(response.data['sensor_id'][0].code, 'required')
        self.assertEqual(response.data['data'][0].code, 'required')

    def test_400_sensor_id_invalid(self):
        response = self.client.post(
            path=self.path,
            data={'name': 'fake', 'data': '{}', 'sensor_id': 'not-good'}
        )
        self.assertResponse400(response)
        self.assertEqual(response.data['sensor_id'][0].code, 'invalid')
