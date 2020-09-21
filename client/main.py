import import_string
import requests
from config import CLIENT_UUID, LIBRARY_WRAPPER, SERVER_ENDPOINT


class Main:
    def __init__(self, uuid, wrapper_name, endpoint, timeout=3):
        self.uuid = uuid
        self.timeout = timeout
        self.wrapper_name = wrapper_name
        self.endpoint = endpoint

    def run(self):
        wrapper_class = import_string(self.wrapper_name)
        wrapper = wrapper_class()
        data = {
            "sensor": self.uuid,
            "value": wrapper.gather(),
        }
        requests.post(self.endpoint, data=data, timeout=self.timeout)


if __name__ == "__main__":

    app = Main(CLIENT_UUID, LIBRARY_WRAPPER, SERVER_ENDPOINT)
    app.run()