import numpy as np
import pytest


np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        np.random.randint(0, MAX, size=SIZE),
        np.random.rand(7, 7) * MAX,
    ]
)
def array(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[np.full(SIZE, "A"), TypeError]])
def array_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
