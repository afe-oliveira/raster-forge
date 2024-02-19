import pytest


@pytest.fixture(params=[1, 10])
def scale(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["A", TypeError]])
def scale_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
