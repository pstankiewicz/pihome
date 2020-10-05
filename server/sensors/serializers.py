from .models import Sensor, SensorData
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())
    class Meta:
        model = SensorData
        fields = [
            "value",
            "sensor",
            "datetime",
        ]
