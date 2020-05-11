from django.contrib import admin

from web.ruuvitags.models import Event, Sensor, StructuredEvent


class EventAdmin(admin.ModelAdmin):
    fields = ['data', 'created', 'updated']
    readonly_fields = ['id', 'created', 'updated']
    list_display = ['id', 'created', 'updated']
    ordering = ['-created']


class StructuredEventAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'updated']
    list_display = ['id', 'temperature', 'created', 'updated']


class SensorAdmin(admin.ModelAdmin):
    fields = ['name', 'mac_address', 'created', 'updated']
    readonly_fields = ['id', 'mac_address', 'created', 'updated']
    list_display = ['id', 'mac_address', 'created', 'updated']

    def __str__(self):
        return self.name


admin.site.register(Event, EventAdmin)
admin.site.register(StructuredEvent, StructuredEventAdmin)
admin.site.register(Sensor, SensorAdmin)
