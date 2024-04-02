import numpy as np
import pytest

from rforge.library.containers.layer import Layer

np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        None,
        Layer(np.random.randint(0, MAX, size=SIZE)),
        np.random.randint(0, MAX, size=SIZE),
        Layer(np.random.rand(7, 7) * MAX),
        np.random.rand(7, 7) * MAX,
    ]
)
def alpha(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[np.full(SIZE, "A"), TypeError]])
def alpha_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
