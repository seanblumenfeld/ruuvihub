from rest_framework.reverse import reverse

from web.tests.factories.sensor import SensorFactory
from web.tests.factories.user import UserFactory
from web.tests.helpers import BaseTestCase, get_api_token


class SensorDetailTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.sensor = SensorFactory(user=self.user)
        self.path = reverse('sensors-detail', args=(self.sensor.id,))
        token = get_api_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_get_sensor(self):
        response = self.client.get(path=self.path)
        self.assertResponse200(
            response, data_contains={'id': self.sensor.id_str, 'name': self.sensor.name}
        )


class SensorViewSetTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = reverse('sensors-list')

    def setUp(self):
        super().setUp()
        token = get_api_token()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_create_sensor(self):
        mac = 'DU:MM:YD:AT:A9:3D'
        response = self.client.post(
            path=self.path,
            data={'mac': mac},
        )
        self.assertResponse201(response)
        self.assertEqual(response.data['mac'], mac)

    def test_new_sensor_creates_sensor_location(self):
        mac = 'DU:MM:YD:AT:A9:3D'
        response = self.client.post(
            path=self.path,
            data={'mac': mac},
        )
        self.assertResponse201(response)

    def test_400_when_params_not_provided(self):
        response = self.client.post(path=self.path)
        self.assertResponse400(response)
        self.assertEqual(response.data['mac'][0].code, 'required')

    def test_400_mac_invalid(self):
        response = self.client.post(
            path=self.path,
            data={'mac': 'not-good'}
        )
        self.assertResponse400(response)
        self.assertEqual(response.data['mac'][0].code, 'invalid')
