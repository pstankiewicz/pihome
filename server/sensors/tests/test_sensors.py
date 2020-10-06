from freezegun import freeze_time
import uuid

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..factories import SensorDataFactory, SensorFactory
from ..models import SensorData


class SensorDataTestCase(TestCase):
    def setUp(self):
        self.sensor = SensorFactory()
        self.client = APIClient()

    def test_incorrect_sensor_uuid_post_causes_400(self):
        # Arrange
        dummy_uuid = str(uuid.uuid4())
        data = {
            "sensor": dummy_uuid,
            "value": 0,
        }

        # Act
        response = self.client.post("/api/sensor-data/", data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(SensorData.objects.count(), 0)

    def test_correct_sensor_uuid_post_causes_201_and_creates_object(self):
        # Arrange
        data = {
            "sensor": self.sensor.uuid,
            "value": 0,
        }

        # Act
        response = self.client.post("/api/sensor-data/", data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SensorData.objects.count(), 1)

    def test_get_should_return_sensor_data(self):
        # Arrange
        new_sensor = SensorFactory.create()
        data = {
            "sensor": new_sensor.uuid,
        }
        SensorDataFactory.create_batch(
            5,
            sensor=new_sensor,
        )

        # Act
        response = self.client.get("/api/sensor-data/", data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    @freeze_time("2020-10-03")
    def test_get_should_filter_data_by_date_from(self):
        # Arrange
        new_sensor = SensorFactory.create()
        data = {
            "sensor": new_sensor.uuid,
            "date_from": "2020-10-02",
        }
        SensorDataFactory.create_batch(
            5,
            sensor=new_sensor,
        )

        # Act
        response = self.client.get("/api/sensor-data/", data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    @freeze_time("2020-10-03")
    def test_get_should_filter_data_by_date_to(self):
        # Arrange
        new_sensor = SensorFactory.create()
        data = {
            "sensor": new_sensor.uuid,
            "date_to": "2020-10-04",
        }
        SensorDataFactory.create_batch(
            5,
            sensor=new_sensor,
        )

        # Act
        response = self.client.get("/api/sensor-data/", data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_get_should_filter_data_by_date_from_and_date_to(self):
        # Arrange
        new_sensor = SensorFactory.create()
        data = {
            "sensor": new_sensor.uuid,
            "date_from": "2020-10-05",
            "date_to": "2020-10-06",
        }
        for date in [
            "2020-10-04",
            "2020-10-05",
            "2020-10-06",
            "2020-10-07",
        ]:
            with freeze_time(date):
                SensorDataFactory.create_batch(
                    3,
                    sensor=new_sensor,
                )

        # Act
        response = self.client.get("/api/sensor-data/", data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @freeze_time("2020-10-03")
    def test_get_should_receive_data_with_correct_datetime_format(self):
        # Arrange
        new_sensor = SensorFactory.create()
        data = {
            "sensor": new_sensor.uuid,
        }
        SensorDataFactory.create(
            sensor=new_sensor,
        )

        # Act
        response = self.client.get("/api/sensor-data/", data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]["datetime"], "2020-10-03 00:00:00")
