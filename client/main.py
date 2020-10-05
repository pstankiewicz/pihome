from urllib.parse import urljoin

import import_string
import requests
from requests.exceptions import ConnectionError

from config import AUTH_TOKEN, LIBRARY_WRAPPERS_AND_SENSOR_UUIDS, SERVER_ENDPOINT
from wrappers.exceptions import WrapperException


class Main:
    def __init__(self, wrapper_names, endpoint, timeout=3):
        self.timeout = timeout
        self.wrapper_names = wrapper_names
        self.endpoint = urljoin(endpoint, "api/sensor-data/")

    def run(self):
        for wrapper_name, sensor_uuid in self.wrapper_names:
            wrapper_class = import_string(wrapper_name)
            wrapper = wrapper_class()
            headers = {"Authorization": "Token {}".format(AUTH_TOKEN)}
            try:
                data = {
                    "sensor": sensor_uuid,
                    "value": wrapper.gather(),
                }
                try:
                    result = requests.post(
                        self.endpoint,
                        data=data,
                        timeout=self.timeout,
                        headers=headers,
                    )
                except ConnectionError as e:
                    print(e)
                else:
                    if result.status_code != 201:
                        print(result.text)
            except WrapperException as e:
                print(e)


if __name__ == "__main__":

    app = Main(LIBRARY_WRAPPERS_AND_SENSOR_UUIDS, SERVER_ENDPOINT)
    app.run()
