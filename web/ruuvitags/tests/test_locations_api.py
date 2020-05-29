from rest_framework.reverse import reverse

from web.tests.factories.location import LocationFactory
from web.tests.factories.sensor import SensorFactory
from web.tests.factories.user import UserFactory
from web.tests.helpers import BaseTestCase, get_api_token


class LocationDetailTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.location = LocationFactory(sensor__user=self.user)
        self.path = reverse('locations-detail', args=(self.location.id,))
        token = get_api_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_get_location(self):
        response = self.client.get(path=self.path)
        self.assertResponse200(
            response, data_contains={'id': self.location.id_str, 'name': self.location.name}
        )


class LocationViewSetTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = reverse('locations-list')

    def setUp(self):
        super().setUp()
        token = get_api_token()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")
        self.sensor = SensorFactory()

    def test_can_create_location(self):
        response = self.client.post(
            path=self.path,
            data={'sensor': self.sensor.id},
        )
        self.assertResponse201(response)
        self.assertEqual(response.data['sensor'], self.sensor.id)

    def test_400_when_params_not_provided(self):
        response = self.client.post(path=self.path)
        self.assertResponse400(response)
        self.assertEqual(response.data['sensor'][0].code, 'required')

    def test_400_for_duplicate_location_name(self):
        response = self.client.post(
            path=self.path, data={'name': 'location-1', 'sensor': self.sensor.id}
        )
        self.assertResponse201(response)
        response = self.client.post(
            path=self.path, data={'name': 'location-1', 'sensor': self.sensor.id}
        )
        self.assertResponse400(response)
        self.assertEqual(response.data['name'][0].code, 'unique')
