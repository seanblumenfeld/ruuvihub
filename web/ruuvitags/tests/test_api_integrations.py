from rest_framework.reverse import reverse

from web.ruuvitags.models import Event
from web.ruuvitags.tests.helpers import DATA_FORMAT_5_EXAMPLE
from web.tests.factories.event import EventFactory
from web.tests.factories.location import LocationFactory
from web.tests.factories.sensor import SensorFactory
from web.tests.factories.user import UserFactory
from web.tests.helpers import BaseTestCase, get_api_token


class CombinedApiTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        token = get_api_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_move_sensor_to_new_location(self):
        mac = DATA_FORMAT_5_EXAMPLE['mac']

        # Given sensor-1 is in location-1 with multiple events attributed to it
        sensor_1 = SensorFactory(name='sensor-1', mac=mac, user=self.user)
        location_1 = LocationFactory(name='location-1', sensor=sensor_1)
        EventFactory.create_batch(size=5, location=location_1)

        # When sensor-1 is moved to location-2
        location_2 = LocationFactory(name='location-2', sensor=sensor_1)
        # And then a new broadcast is made
        response = self.client.post(path=reverse('broadcasts-list'), data=DATA_FORMAT_5_EXAMPLE)

        # Then the new broadcast is attributed to location-2
        self.assertResponse201(response, data_contains={'location': location_2.id})
        self.assertEqual(Event.objects.filter(location=location_2).count(), 1)
