from web.tests.factories.structured_event import StructuredEventFactory
from web.tests.helpers import BaseTestCase


class StructuredEventTests(BaseTestCase):

    def test_mac_address(self):
        structured_event = StructuredEventFactory(mac='dummydata93d')
        self.assertEqual(structured_event.mac_address, 'DU:MM:YD:AT:A9:3D')
