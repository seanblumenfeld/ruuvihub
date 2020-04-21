from django.test import TestCase

from web.ruuvitags.models import Sensors, Events
from web.ruuvitags.services import find_and_save_sensors, save_sensor_event
from web.ruuvitags.tests.helpers import FakeRuuviTagSensor


class FindSensorsTests(TestCase):

    def test_returns_all_sensors(self):
        sensors = find_and_save_sensors(FakeRuuviTagSensor)
        self.assertEqual(len(sensors), 2)

    def test_persists_new_sensors(self):
        find_and_save_sensors(FakeRuuviTagSensor)
        self.assertEqual(Sensors.objects.count(), 2)

    def test_does_not_persist_duplicate_sensor(self):
        find_and_save_sensors(FakeRuuviTagSensor)
        find_and_save_sensors(FakeRuuviTagSensor)
        self.assertEqual(Sensors.objects.count(), 2)


class SimpleSaveSensorDataSensorsTests(TestCase):

    def test_persists_new_sensors_event(self):
        save_sensor_event(mac='fake-mac', data={'fake': 'data'})
        self.assertEqual(Events.objects.count(), 1)
