import factory

from .models import Sensor, SensorData


class SensorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sensor


class SensorDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SensorData
