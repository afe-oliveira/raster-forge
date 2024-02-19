import pytest


@pytest.fixture(params=["NDVI", "NDWI"])
def index_id(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["AAAA", Exception], ["BBBB", Exception]])
def index_id_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
