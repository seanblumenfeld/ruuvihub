from unittest import TestCase

import requests_mock

from services.ruuvitags.watch_sensor_events import post_sensor_event, EVENT_API, SENSOR_API, \
    get_sensor_mac_addresses


class Tests(TestCase):
    SENSORS_API_RESPONSE = [
        {
            'id': 'd88766c0-e18b-43ea-9b2c-67b654be983c',
            'updated': '2020-05-07T13:20:50.668580Z',
            'created': '2020-05-07T13:20:50.668634Z',
            'name': 'My first sensor',
            'sensor_id': 'FE:F6:ED:CF:47:F3',
        }
    ]

    @requests_mock.Mocker()
    def test_post_to_events_api(self, _requests_mock):
        _requests_mock.post(EVENT_API, status_code=201)
        post_sensor_event(mac='fake-mac', data='json-data')
        self.assertTrue(_requests_mock.called)

    @requests_mock.Mocker()
    def test_get_sensor_mac_addresses(self, _requests_mock):
        _requests_mock.get(SENSOR_API, json=self.SENSORS_API_RESPONSE)
        mac_addresses = get_sensor_mac_addresses()
        self.assertTrue(_requests_mock.called)
        self.assertEqual(mac_addresses, ['FE:F6:ED:CF:47:F3'])
