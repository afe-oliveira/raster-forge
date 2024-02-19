import numpy as np
import pytest


np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(params=[(1, 2, 3, 4, 5, 6), (1, -2, 3, -4, 5, -6)])
def transform(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[(1, 2, 3), TypeError], [(1, "B", 3), TypeError]])
def transform_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
