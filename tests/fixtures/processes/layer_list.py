import numpy as np
import pytest

from rforge.lib.containers.layer import Layer

np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        [Layer(np.random.randint(0, MAX, size=SIZE)) for _ in range(5)],
        [np.random.randint(0, MAX, size=SIZE) for _ in range(5)],
        [Layer(np.random.rand(7, 7) * MAX) for _ in range(5)],
        [np.random.rand(7, 7) * MAX for _ in range(5)],
    ]
)
def layer_list(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[[np.full(SIZE, "A") for _ in range(5)], TypeError]])
def layer_list_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
