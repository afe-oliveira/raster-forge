import numpy as np
import pytest


np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        {"left": 10000, "top": 20000, "right": 30000, "bottom": 40000},
        {"left": 10000.0, "top": 20000.0, "right": 30000.0, "bottom": 40000.0},
    ]
)
def bounds(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        [{"left": "10000", "top": 20000, "right": "30000", "bottom": 40000}, TypeError],
        [{"AAAA": 10000, "top": 20000, "CCCC": 30000, "bottom": 40000}, TypeError],
    ]
)
def bounds_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
