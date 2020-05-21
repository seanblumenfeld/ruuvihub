import os
from unittest import TestCase
from unittest.mock import patch

import requests_mock

from services.ruuvitags.watch_sensor_events import watch_sensor_events


@patch.dict(os.environ, {
    'PROTOCOL': 'http', 'HOST': 'localhost', 'PORT': '8000', 'ACCESS_TOKEN': 'fake-access-token',
    'REFRESH_TOKEN': 'fake-refresh-token'
})
@requests_mock.Mocker()
class Tests(TestCase):
    uri = 'http://localhost:8000'

    def test_post_to_events_api(self, _requests_mock):
        _requests_mock.register_uri('POST', f'{self.uri}/api/events/', status_code=201)
        response = watch_sensor_events(mac='fake-mac', data='json-data')
        self.assertTrue(_requests_mock.called)
        self.assertEqual(response.status_code, 201)

    def test_api_token_refresh(self, _requests_mock):
        _requests_mock.register_uri(
            'POST', f'{self.uri}/api/events/', [{'status_code': 401}, {'status_code': 201}]
        )
        _requests_mock.register_uri(
            'POST', f'{self.uri}/api/token/refresh/', status_code=200,
            json={'refresh': 'fake-refresh-token', 'access': 'fake-access-token'},
        )
        response = watch_sensor_events(mac='fake-mac', data='json-data')
        self.assertEqual(_requests_mock.call_count, 3)
        self.assertEqual(_requests_mock.request_history[0].path, '/api/events/')
        self.assertEqual(_requests_mock.request_history[1].path, '/api/token/refresh/')
        self.assertEqual(_requests_mock.request_history[2].path, '/api/events/')
        self.assertEqual(response.status_code, 201)
