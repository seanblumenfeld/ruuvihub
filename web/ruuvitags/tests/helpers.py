from unittest.mock import create_autospec

from ruuvitag_sensor.ruuvi import RuuviTagSensor

FakeRuuviTagSensor = create_autospec(spec=RuuviTagSensor)
FakeRuuviTagSensor.find_ruuvitags.return_value = {
    'DU:MM:YD:AT:A9:3D': {
        'data_format': 2,
        'humidity': 30.0,
        'identifier': None,
        'pressure': 995.0,
        'temperature': 24.0
    },
    'NO:TS:UP:PO:RT:ED': {
        'data_format': 2,
        'humidity': 30.0,
        'identifier': None,
        'pressure': 995.0,
        'temperature': 24.0
    }
}