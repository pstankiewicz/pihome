from django.contrib import admin
from .models import Alert, AlertLog, Sensor, SensorData


class SensorDataInline(admin.TabularInline):
    model = SensorData
    readonly_fields = [
        "datetime",
    ]
    fields = [
        "value",
        "datetime",
    ]
    ordering = ["datetime"]


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "uuid",
    ]
    readonly_fields = [
        "uuid",
    ]
    inlines = [
        SensorDataInline,
    ]


admin.site.register(SensorData)
admin.site.register(Alert)
admin.site.register(AlertLog)