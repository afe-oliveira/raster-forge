import pickle

import pytest

with open("tests/files/height.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_height(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_height_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
