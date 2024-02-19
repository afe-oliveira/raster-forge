import numpy as np
import pytest


np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(params=[10000, 10000.0])
def no_data(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["A", TypeError]])
def no_data_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
