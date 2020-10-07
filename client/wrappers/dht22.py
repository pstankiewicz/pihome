import adafruit_dht
import board
import time

from .exceptions import WrapperException


class Dht22WrapperTemperature:
    def __init__(self):
        self.sensor = adafruit_dht.DHT22(board.D4)
        self.sleep_time = 2.0
        self.retry_count = 10

    def gather(self):
        """Need to make loop and sleep because of DHT22 sensor instability"""
        result = None
        for _ in range(self.retry_count):
            try:
                result = self._get_reading()
                break
            except RuntimeError as e:
                print(e)
                time.sleep(self.sleep_time)
                continue

        self.sensor.exit()
        if result:
            return result

        raise WrapperException("Can't read DHT22")

    def _get_reading(self):
        return self.sensor.temperature


class Dht22WrapperHumidity(Dht22WrapperTemperature):
    def _get_reading(self):
        return self.sensor.humidity
