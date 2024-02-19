import numpy as np
import pytest

np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        tuple(sorted(np.random.randint(0, MAX, size=2))),
        tuple(sorted(np.random.rand(2) * MAX)),
    ]
)
def thresholds(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        [np.full(2, "A"), TypeError],
        [tuple(sorted(np.random.randint(0, MAX, size=2), reverse=True)), TypeError],
        [tuple(sorted(np.random.rand(2) * MAX, reverse=True)), TypeError],
    ]
)
def thresholds_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
