from django import template
from sensors.models import Sensor

register = template.Library()


@register.inclusion_tag("sensors/menu.html")
def sensors_menu():
    return {
        "sensors": Sensor.objects.all(),
    }


@register.inclusion_tag("sensors/preview.html")
def sensors_preview():
    return {
        "sensors": Sensor.objects.all(),
    }