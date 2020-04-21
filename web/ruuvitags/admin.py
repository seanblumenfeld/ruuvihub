from django.contrib import admin

from web.ruuvitags.models import Events, Sensors


class EventsAdmin(admin.ModelAdmin):
    fields = ['data']


class SensorsAdmin(admin.ModelAdmin):
    fields = ['name', 'sensor_id', 'data']


admin.site.register(Events, EventsAdmin)
admin.site.register(Sensors, SensorsAdmin)
