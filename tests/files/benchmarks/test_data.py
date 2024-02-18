import pickle


class TestData:

    _data: dict

    def __init__(self):
        self._data = {}

    @property
    def data(self):
        return self._data

    def add(self, name, item):
        self._data[name] = item

    def clear(self):
        self._data = {}

    def dump(self, file: str):
        with open(file, "wb") as f:
            pickle.dump(self._data, f)


COMPOSITE_TEST_DATA = TestData()

DISTANCE_TEST_DATA = TestData()

FUEL_TEST_DATA = TestData()

HEIGHT_TEST_DATA = TestData()

INDEX_TEST_DATA = TestData()

SLOPE_TEST_DATA = TestData()
ASPECT_TEST_DATA = TestData()
