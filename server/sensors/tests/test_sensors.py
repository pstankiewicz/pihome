import uuid

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..factories import SensorDataFactory, SensorFactory
from ..models import SensorData


class SensorsTestCase(TestCase):
    def setUp(self):
        self.sensor = SensorFactory()
        self.client = APIClient()

    def test_incorrect_sensor_uuid_post_causes_400(self):
        # Arrange
        dummy_uuid = str(uuid.uuid4())
        data = {
            'sensor': dummy_uuid,
            'value': 0,
        }

        # Act
        response = self.client.post('/api/sensor-data/', data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(SensorData.objects.count(), 0)

    def test_correct_sensor_uuid_post_causes_201_and_creates_object(self):
        # Arrange
        data = {
            'sensor': self.sensor.uuid,
            'value': 0,
        }

        # Act
        response = self.client.post('/api/sensor-data/', data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SensorData.objects.count(), 1)
