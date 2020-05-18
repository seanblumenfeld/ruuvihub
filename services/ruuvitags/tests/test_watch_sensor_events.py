from unittest import TestCase

import requests_mock

from services.ruuvitags.watch_sensor_events import post_sensor_event


class Tests(TestCase):

    @requests_mock.Mocker()
    def test_post_to_events_api(self, _requests_mock):
        _requests_mock.post('http://localhost:8000/api/events/', status_code=201)
        response = post_sensor_event(mac='fake-mac', data='json-data')
        self.assertTrue(_requests_mock.called)
        self.assertEqual(response.status_code, 201)
