from django.contrib import admin

from web.ruuvitags.models import Event, Sensor


class EventsAdmin(admin.ModelAdmin):
    fields = ['data']


class SensorsAdmin(admin.ModelAdmin):
    fields = ['name', 'sensor_id', 'data']


admin.site.register(Event, EventsAdmin)
admin.site.register(Sensor, SensorsAdmin)
