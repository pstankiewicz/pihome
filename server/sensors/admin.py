from django.contrib import admin
from .models import Sensor, SensorData


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    fields = ["name", "uuid", ]
    readonly_fields = ["uuid", ]


admin.site.register(SensorData)