from .models import Sensor, SensorData
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())
    datetime = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True
    )

    class Meta:
        model = SensorData
        fields = [
            "value",
            "sensor",
            "datetime",
        ]

    def validate(self, attrs):
        if not attrs["sensor"].active:
            raise serializers.ValidationError(
                "Sensor %s is not active" % attrs["sensor"]
            )
        return attrs
