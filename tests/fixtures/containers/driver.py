import numpy as np
import pytest


np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(params=["AAAA", "BBBB", "CCCC", "DDDD"])
def driver(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[100, TypeError], [100.0, TypeError]])
def driver_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
