from unittest import TestCase
from unittest.mock import patch

import requests

from services.ruuvitags.watch_sensor_events import save_sensor_event, EVENTS_API


class Tests(TestCase):

    @patch('services.ruuvitags.watch_sensor_events.requests', autospec=requests)
    def test_post_to_events_api(self, requests_patch):
        save_sensor_event(mac='fake-mac', data='json-data')
        requests_patch.post.assert_called()
        self.assertEqual(requests_patch.post.call_args[0][0], EVENTS_API)
