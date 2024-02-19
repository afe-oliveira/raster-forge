import pytest


@pytest.fixture(params=[3, 5])
def mask_size(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["A", TypeError], [1, TypeError]])
def mask_size_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
