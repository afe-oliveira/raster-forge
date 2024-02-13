import pickle
import pytest

with open("tests/files/distance.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_distance(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_distance_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
