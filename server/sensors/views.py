from datetime import datetime, timedelta
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
        period = self.request.query_params.get("period", None)
        date_from = self.request.query_params.get("date_from", None)
        date_to = self.request.query_params.get("date_to", None)
        if period:
            date_from, date_to = self._extract_dates_from_period(period)
        if sensor_uuid:
            queryset = queryset.filter(sensor__uuid=sensor_uuid)
        if date_from:
            queryset = queryset.filter(datetime__gte=date_from)
        if date_to:
            queryset = queryset.filter(datetime__lte=date_to)

        return queryset

    def _extract_dates_from_period(self, period):
        date_from = datetime.now().replace(hour=0, minute=0, second=0)
        date_to = datetime.now().replace(hour=23, minute=59, second=59)

        if period == "today":
            date_from = datetime.now().replace(hour=0, minute=0, second=0)
            date_to = datetime.now().replace(hour=23, minute=59, second=59)
        if period == "yesterday":
            date_from = datetime.now() - timedelta(days=1)
            date_from = date_from.replace(hour=0, minute=0, second=0)
            date_to = date_from
            date_to = date_to.replace(hour=23, minute=59, second=59)
        if period == "this-week":
            date_from = datetime.now() - timedelta(days=datetime.now().weekday())
            date_to = date_from + timedelta(days=6)
            date_from = date_from.replace(hour=0, minute=0, second=0)
            date_to = date_to.replace(hour=23, minute=59, second=59)
        if period == "last-week":
            date_from = (
                datetime.now()
                - timedelta(days=datetime.now().weekday())
                - timedelta(days=7)
            )
            date_to = date_from + timedelta(days=6)
            date_from = date_from.replace(hour=0, minute=0, second=0)
            date_to = date_to.replace(hour=23, minute=59, second=59)

        return str(date_from), str(date_to)


class SensorDetail(DetailView):

    model = Sensor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sensor_data"] = self.object.sensordata_set.all().order_by("datetime")
        return context
