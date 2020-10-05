from django.views.generic import DetailView
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from .models import Sensor, SensorData
from .serializers import SensorDataSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    authentication_classes = [
        TokenAuthentication,
    ]
    queryset = SensorData.objects.all().order_by("datetime")
    serializer_class = SensorDataSerializer
    http_method_names = [
        "get",
        "post",
    ]

    def get_queryset(self):
        queryset = SensorData.objects.all().order_by("datetime")
        sensor_uuid = self.request.query_params.get("sensor", None)
        if sensor_uuid:
            queryset = queryset.filter(sensor__uuid=sensor_uuid)
        return queryset


class SensorDetail(DetailView):

    model = Sensor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sensor_data"] = self.object.sensordata_set.all().order_by("datetime")
        return context