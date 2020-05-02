from rest_framework.reverse import reverse

from web.tests.factories.sensor import SensorFactory
from web.tests.helpers import BaseTestCase


class SensorDetailTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.sensor = SensorFactory()
        self.path = reverse('sensors-detail', args=(self.sensor.id,))

    def test_can_get_event(self):
        response = self.client.get(path=self.path)
        self.assertResponse200(
            response, data_contains={'id': self.sensor.id_str, 'data': self.sensor.data}
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
