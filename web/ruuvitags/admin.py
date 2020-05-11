from django.contrib import admin

from web.ruuvitags.models import Event, Sensor


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = [
        'data_format', 'mac', 'humidity', 'temperature', 'pressure', 'acceleration',
        'acceleration_x', 'acceleration_y', 'acceleration_z', 'tx_power', 'battery',
        'movement_counter', 'measurement_sequence_number', 'created', 'updated'
    ]
    readonly_fields = [
        'data_format', 'humidity', 'temperature', 'pressure', 'acceleration', 'acceleration_x',
        'acceleration_y', 'acceleration_z', 'tx_power', 'battery', 'movement_counter',
        'measurement_sequence_number', 'mac', 'created', 'updated'
    ]
    list_display = ['id', 'mac_address', 'data_format', 'temperature', 'created']
    ordering = ['-created']


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    fields = ['name', 'mac_address', 'created', 'updated']
    readonly_fields = ['id', 'mac_address', 'created', 'updated']
    list_display = ['id', 'mac_address', 'created', 'updated']

    def __str__(self):
        return self.name
