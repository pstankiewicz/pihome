from urllib.parse import urljoin

import import_string
import requests

from config import LIBRARY_WRAPPER, SENSOR_UUID, SERVER_ENDPOINT


class Main:
    def __init__(self, uuid, wrapper_name, endpoint, timeout=3):
        self.uuid = uuid
        self.timeout = timeout
        self.wrapper_name = wrapper_name
        self.endpoint = urljoin(endpoint, "api/sensor-data/")

    def run(self):
        wrapper_class = import_string(self.wrapper_name)
        wrapper = wrapper_class()
        data = {
            "sensor": self.uuid,
            "value": wrapper.gather(),
        }
        result = requests.post(self.endpoint, data=data, timeout=self.timeout)
        if result.status_code != 201:
            print(result.text)


if __name__ == "__main__":

    app = Main(SENSOR_UUID, LIBRARY_WRAPPER, SERVER_ENDPOINT)
    app.run()
