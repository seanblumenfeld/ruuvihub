from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from web.ruuvitags.views import EventViewSet, SensorViewSet


class EventViewSetTests(APITestCase):

    def setUp(self):
        super().setUp()
        self.path = reverse(f'{EventViewSet.url_prefix}-list')

    def test_can_create_event(self):
        response = self.client.post(path=self.path, data={'data': '{}'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data)

    def test_400_when_no_data_provided(self):
        response = self.client.post(path=self.path)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['data'][0].code, 'required')

    def test_400_for_invalid_json_data(self):
        response = self.client.post(path=self.path, data={'data': '{'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['data'][0].code, 'invalid')


class SensorViewSetTests(APITestCase):

    def setUp(self):
        super().setUp()
        self.path = reverse(f'{SensorViewSet.url_prefix}-list')

    def test_can_create_sensor(self):
        name = 'new-sensor'
        response = self.client.post(
            path=self.path,
            data={'name': name}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['name'], name)

    def test_400_when_params_not_provided(self):
        response = self.client.post(path=self.path)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0].code, 'required')
