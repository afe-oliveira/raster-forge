import pytest


@pytest.fixture(params=["degrees", "radians"])
def angle_units(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["meters", TypeError]])
def angle_units_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
