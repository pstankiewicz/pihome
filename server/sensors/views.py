from rest_framework import permissions, viewsets

from .models import SensorData
from .serializers import SensorDataSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all().order_by('-datetime')
    serializer_class = SensorDataSerializer
    # permission_classes = [permissions.IsAuthenticated]
