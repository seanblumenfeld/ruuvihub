import os
from unittest import TestCase
from unittest.mock import patch

import requests_mock

from services.ruuvitags.ruuvitag_gateway import ruuvitag_sensor_watch_sensor_events


@patch.dict(os.environ, {
    'PROTOCOL': 'http', 'HOST': 'localhost', 'PORT': '8000', 'ACCESS_TOKEN': 'fake-access-token',
    'REFRESH_TOKEN': 'fake-refresh-token'
})
@requests_mock.Mocker()
class Tests(TestCase):
    uri = 'http://localhost:8000'

    @patch('services.ruuvitags.ruuvitag_gateway.ignore_event', return_value=False)
    def test_post_to_events_api(self, _requests_mock, _ignore_event_mock):
        _requests_mock.register_uri(
            'POST', f'{self.uri}/api/ruuvitags/broadcasts/', status_code=201
        )
        response = ruuvitag_sensor_watch_sensor_events(data=('fake-mac', {'fake': 'json-data'}))
        self.assertTrue(_requests_mock.called)
        self.assertEqual(response.status_code, 201)

    @patch('services.ruuvitags.ruuvitag_gateway.ignore_event', return_value=True)
    def test_ignore_event_and_do_not_post_to_events_api(self, _requests_mock, _ignore_event_mock):
        _requests_mock.register_uri(
            'POST', f'{self.uri}/api/ruuvitags/broadcasts/', status_code=201
        )
        response = ruuvitag_sensor_watch_sensor_events(data=('fake-mac', {'fake': 'json-data'}))
        self.assertFalse(_requests_mock.called)
        self.assertIsNone(response)

    @patch('services.ruuvitags.ruuvitag_gateway.ignore_event', return_value=False)
    def test_api_token_refresh(self, _requests_mock, _ignore_event_mock):
        _requests_mock.register_uri(
            'POST', f'{self.uri}/api/ruuvitags/broadcasts/',
            [{'status_code': 401}, {'status_code': 201}]
        )
        _requests_mock.register_uri(
            'POST', f'{self.uri}/api/token/refresh/', status_code=200,
            json={'refresh': 'fake-refresh-token', 'access': 'fake-access-token'},
        )
        response = ruuvitag_sensor_watch_sensor_events(data=('fake-mac', {'fake': 'json-data'}))
        self.assertEqual(_requests_mock.call_count, 3)
        self.assertEqual(_requests_mock.request_history[0].path, '/api/ruuvitags/broadcasts/')
        self.assertEqual(_requests_mock.request_history[1].path, '/api/token/refresh/')
        self.assertEqual(_requests_mock.request_history[2].path, '/api/ruuvitags/broadcasts/')
        self.assertEqual(response.status_code, 201)
