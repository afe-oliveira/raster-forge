import pytest


@pytest.fixture(params=[])
def data_topography(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_topography_errors(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
