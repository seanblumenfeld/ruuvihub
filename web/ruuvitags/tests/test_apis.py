from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from web.ruuvitags.views import CreateEventAPI


class CreateEventApiTestCase(APITestCase):

    def setUp(self):
        super().setUp()
        self.path = reverse(CreateEventAPI.name)

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
