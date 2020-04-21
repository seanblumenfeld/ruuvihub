from rest_framework.reverse import reverse

from web.ruuvitags.views import EventViewSet, SensorViewSet
from web.tests.helpers import BaseTestCase


class EventViewSetTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.path = reverse(f'{EventViewSet.url_prefix}-list')

    def test_can_create_event(self):
        response = self.client.post(path=self.path, data={'data': '{}'})
        self.assertResponse201(response, data={})

    def test_400_when_no_data_provided(self):
        response = self.client.post(path=self.path)
        self.assertResponse400(response)
        self.assertEqual(response.data['data'][0].code, 'required')

    def test_400_for_invalid_json_data(self):
        response = self.client.post(path=self.path, data={'data': '{'})
        self.assertResponse400(response)
        self.assertEqual(response.data['data'][0].code, 'invalid')


class SensorViewSetTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.path = reverse(f'{SensorViewSet.url_prefix}-list')

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
