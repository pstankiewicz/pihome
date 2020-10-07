from random import randint


class DummyWrapper:
    def gather(self):
        return randint(0, 100)
