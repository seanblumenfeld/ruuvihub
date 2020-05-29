from datetime import datetime

from pytz import UTC
from rest_framework.reverse import reverse

from web.ruuvitags.models import Event
from web.tests.factories.event import EventFactory
from web.tests.factories.location import LocationFactory
from web.tests.factories.user import UserFactory
from web.tests.helpers import BaseTestCase, get_api_token


class EventCreateTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = reverse('events-list')

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        token = get_api_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_create_event(self):
        location = LocationFactory()
        response = self.client.post(
            path=self.path,
            data={
                'data_format': 5,
                'humidity': 30.27,
                'temperature': 26.24,
                'pressure': 1013.49,
                'acceleration': 990.1030249423542,
                'acceleration_x': 56,
                'acceleration_y': -32,
                'acceleration_z': 988,
                'tx_power': 4,
                'battery': 3193,
                'movement_counter': 21,
                'measurement_sequence_number': 963,
                'mac': 'DU:MM:YD:AT:A9:3D',
                'location': location.id
            }
        )
        self.assertResponse201(response)
        self.assertEqual(Event.objects.filter(location=location).count(), 1)

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


class EventListTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        token = get_api_token()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")

    def test_can_list_events(self):
        EventFactory.create_batch(size=4)
        response = self.client.get(path=reverse('events-list'))
        self.assertResponse200(response)
        self.assertEqual(len(response.data), 4)

    def test_filter_events(self):
        location = LocationFactory()
        EventFactory.create_batch(size=2, location=location)
        EventFactory.create_batch(size=2)
        response = self.client.get(path=reverse('events-list') + f'?location={location.id}')
        self.assertResponse200(response)
        self.assertEqual(len(response.data), 2)

    def test_filter_created_after(self):
        EventFactory.create_batch(size=3, created=datetime(year=2020, month=5, day=1, tzinfo=UTC))
        EventFactory.create_batch(size=1, created=datetime(year=2020, month=5, day=3, tzinfo=UTC))
        response = self.client.get(
            path=reverse('events-list'),
            data={'created__gte': datetime(year=2020, month=5, day=2, tzinfo=UTC)}
        )

        self.assertResponse200(response)
        self.assertEqual(len(response.data), 1)


class EventDetailTests(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        token = get_api_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")
        self.event = EventFactory(location__sensor__user=self.user)
        self.path = reverse('events-detail', args=(self.event.id,))

    def test_can_get_event(self):
        response = self.client.get(path=self.path)
        self.assertResponse200(
            response, data_contains={'id': self.event.id_str}
        )
