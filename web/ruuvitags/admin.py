from django.contrib import admin
from rangefilter.filter import DateTimeRangeFilter

from web.ruuvitags.models import Event, Sensor, Location


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = [
        'data_format', 'humidity', 'temperature', 'pressure', 'acceleration',
        'acceleration_x', 'acceleration_y', 'acceleration_z', 'tx_power', 'battery',
        'movement_counter', 'measurement_sequence_number', 'location', 'created', 'updated'
    ]
    readonly_fields = [
        'data_format', 'humidity', 'temperature', 'pressure', 'acceleration', 'acceleration_x',
        'acceleration_y', 'acceleration_z', 'tx_power', 'battery', 'movement_counter',
        'measurement_sequence_number', 'created', 'updated'
    ]
    list_display = ['sensor_name', 'location_name', 'data_format', 'temperature', 'created']
    list_filter = [('created', DateTimeRangeFilter)]
    ordering = ['-created']

    def location_name(self, obj):
        return obj.location.name

    def sensor_name(self, obj):
        return obj.location.sensor.name


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ['name', 'sensor', 'created', 'updated']
    readonly_fields = ['id', 'created', 'updated']
    list_display = ['sensor_name', 'name', 'created', 'updated']
    list_filter = ['name', ('created', DateTimeRangeFilter)]

    def sensor_name(self, obj):
        return obj.sensor.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    fields = ['name', 'mac', 'created', 'updated']
    readonly_fields = ['id', 'mac', 'created', 'updated']
    list_display = ['name', 'mac', 'created', 'updated']
    list_filter = ['name', ('created', DateTimeRangeFilter)]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
