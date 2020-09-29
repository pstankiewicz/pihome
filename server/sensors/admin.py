from django.contrib import admin
from .models import Alert, AlertLog, Sensor, SensorData


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "unit",
        "uuid",
    ]
    readonly_fields = [
        "uuid",
    ]


admin.site.register(SensorData)
admin.site.register(Alert)
admin.site.register(AlertLog)