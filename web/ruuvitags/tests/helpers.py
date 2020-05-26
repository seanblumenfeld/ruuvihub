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

DATA_FORMAT_5_EXAMPLE = {
    "data_format": 5,
    "humidity": 30.27,
    "temperature": 26.24,
    "pressure": 1013.49,
    "acceleration": 990.1030249423542,
    "acceleration_x": 56,
    "acceleration_y": -32,
    "acceleration_z": 988,
    "tx_power": 4,
    "battery": 3193,
    "movement_counter": 21,
    "measurement_sequence_number": 963,
    "mac": 'DU:MM:YD:AT:A9:3D',
    "_updated_at": "2020-05-08T17:43:57.695572"
}


def mac_lower_to_mac_upper(mac):
    return ':'.join([mac[i:i+2].upper() for i in range(0, len(mac), 2)])
