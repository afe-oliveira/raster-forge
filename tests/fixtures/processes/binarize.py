import pytest


@pytest.fixture(params=[True, False])
def binarize(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["True", TypeError], ["False", TypeError]])
def binarize_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
