from unittest import TestCase

import requests_mock

from services.ruuvitags.watch_sensor_events import post_sensor_event, EVENT_API


class Tests(TestCase):

    @requests_mock.Mocker()
    def test_post_to_events_api(self, _requests_mock):
        _requests_mock.post(EVENT_API, status_code=201)
        post_sensor_event(mac='fake-mac', data='json-data')
        self.assertTrue(_requests_mock.called)
