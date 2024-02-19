import pytest


@pytest.fixture(params=[True, False])
def invert(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["True", TypeError], ["False", TypeError]])
def invert_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
