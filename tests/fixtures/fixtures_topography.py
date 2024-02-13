import pickle
import pytest

with open("tests/files/topography.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_topography(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_topography_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
