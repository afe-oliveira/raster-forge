import pytest


@pytest.fixture(params=[])
def data_distance(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_distance_errors(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
