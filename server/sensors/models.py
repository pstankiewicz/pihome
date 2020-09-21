import uuid

from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=64)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return "%s [%s]" % (self.name, self.uuid)


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(default=0, max_digits=10, decimal_places=3)

    def __str__(self):
        return "%s %s" % (self.value, self.datetime)
