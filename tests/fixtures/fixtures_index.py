import pytest


@pytest.fixture(params=[])
def data_index(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_index_errors(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
