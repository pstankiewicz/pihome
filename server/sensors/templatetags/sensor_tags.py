from django import template
from sensors.models import Sensor

register = template.Library()


@register.inclusion_tag("sensors/menu.html")
def sensors_menu():
    return {
        "sensors": Sensor.objects.all(),
    }


@register.inclusion_tag("sensors/preview.html")
def sensors_preview(sensor_uuid=None):
    if sensor_uuid:
        sensors = Sensor.obejects.get(uuid=sensor_uuid)
    else:
        sensors = Sensor.objects.all()
    return {
        "sensors": sensors,
    }
