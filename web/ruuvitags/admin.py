from django.contrib import admin

from web.ruuvitags.models import Event, Sensor


class EventsAdmin(admin.ModelAdmin):
    fields = ['data']


class SensorsAdmin(admin.ModelAdmin):
    fields = ['name', 'mac_address']


admin.site.register(Event, EventsAdmin)
admin.site.register(Sensor, SensorsAdmin)
