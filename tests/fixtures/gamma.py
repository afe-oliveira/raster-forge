import pytest


@pytest.fixture(params=[True, False])
def gamma(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
