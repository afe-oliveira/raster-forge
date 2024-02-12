import pytest


@pytest.fixture(params=[])
def data_composite(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_composite_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
