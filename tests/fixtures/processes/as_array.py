import pytest


@pytest.fixture(params=[True, False])
def as_array(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["True", TypeError], ["False", TypeError]])
def as_array_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
