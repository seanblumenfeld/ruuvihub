from django.contrib import admin

from web.ruuvitags.models import Event, Sensor


class EventsAdmin(admin.ModelAdmin):
    fields = ['data']
    readonly_fields = ['id']


class SensorsAdmin(admin.ModelAdmin):
    fields = ['name', 'mac_address']
    readonly_fields = ['id', 'mac_address']

    def __str__(self):
        return self.name


admin.site.register(Event, EventsAdmin)
admin.site.register(Sensor, SensorsAdmin)
