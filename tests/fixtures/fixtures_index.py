import pickle

import pytest


with open("tests/files/index.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=[])
def data_index(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_index_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
