import uuid

from django.db import models
from djchoices import ChoiceItem, DjangoChoices


class Sensor(models.Model):
    name = models.CharField(max_length=64)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    unit = models.CharField(max_length=32, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s [%s]" % (self.name, self.uuid)

    def last_data(self):
        return self.sensordata_set.last()


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s %s" % (self.value, self.datetime)

    def float_value(self):
        return float(self.value)


class Alert(models.Model):
    class AlertType(DjangoChoices):
        periodic = ChoiceItem("P")
        onetime = ChoiceItem("O")

    class TriggerType(DjangoChoices):
        equals = ChoiceItem("eq")
        not_equals = ChoiceItem("ne")
        greater_than = ChoiceItem("gt")
        greater_than_or_equals = ChoiceItem("gte")
        less_than = ChoiceItem("lt")
        less_than_or_equals = ChoiceItem("lte")

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=1, choices=AlertType.choices)
    name = models.CharField(max_length=64)
    active = models.BooleanField()
    period_minutes = models.IntegerField(blank=True, null=True)
    trigger_type = models.CharField(max_length=3, choices=TriggerType.choices)
    trigger_value = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    trigger_count_for_email = models.IntegerField(default=1)

    def __str__(self):
        return "Alert: %s for sensor: %s" % (self.name, self.sensor)


class Email(models.Model):
    address = models.EmailField()
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)


class AlertLog(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    trigger_value = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    trigger_type = models.CharField(max_length=64)

    def __str__(self):
        return "%s - %s" % (self.sensor, self.trigger_value)
