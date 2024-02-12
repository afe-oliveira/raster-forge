import pytest


@pytest.fixture(params=[])
def data_height(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_height_errors(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
