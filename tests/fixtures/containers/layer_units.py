import pytest


@pytest.fixture(params=["meters", "hertz"])
def layer_units(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[10, TypeError]])
def layer_units_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
