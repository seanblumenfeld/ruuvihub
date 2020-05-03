from web.ruuvitags.models import Sensor, Event
from web.ruuvitags.services import find_and_save_sensors, save_sensor_event
from web.ruuvitags.tests.helpers import FakeRuuviTagSensor
from web.tests.helpers import BaseTestCase


class FindSensorsTests(BaseTestCase):

    def test_returns_all_sensors(self):
        sensors = find_and_save_sensors(FakeRuuviTagSensor)
        self.assertEqual(len(sensors), 2)

    def test_persists_new_sensors(self):
        find_and_save_sensors(FakeRuuviTagSensor)
        self.assertEqual(Sensor.objects.count(), 2)

    def test_does_not_persist_duplicate_sensor(self):
        find_and_save_sensors(FakeRuuviTagSensor)
        find_and_save_sensors(FakeRuuviTagSensor)
        self.assertEqual(Sensor.objects.count(), 2)


class SimpleSaveSensorDataSensorsTests(BaseTestCase):

    def test_persists_new_sensors_event(self):
        save_sensor_event(mac='fake-mac', data={'fake': 'data'})
        # TODO: Fix
        # self.log_capture.check(('root', 'DEBUG', 'a message'))
        self.assertEqual(Event.objects.count(), 1)
