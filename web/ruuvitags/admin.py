from django.contrib import admin

from web.ruuvitags.models import Event, Sensor


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['created', 'updated']
    readonly_fields = ['id', 'created', 'updated']
    list_display = ['id', 'created', 'updated']
    ordering = ['-created']


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    fields = ['name', 'mac_address', 'created', 'updated']
    readonly_fields = ['id', 'mac_address', 'created', 'updated']
    list_display = ['id', 'mac_address', 'created', 'updated']

    def __str__(self):
        return self.name
