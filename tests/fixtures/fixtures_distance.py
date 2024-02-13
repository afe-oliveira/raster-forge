import itertools

import numpy as np
import pytest

from rforge.containers.layer import Layer
from tests.combinations import get_combinations

MAP = {
    "Binary": [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ],
    "Non Binary": [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 10, 10, 10, 10, 10, 0],
        [0, 10, 100, 100, 100, 10, 0],
        [0, 10, 100, 1000, 100, 10, 0],
        [0, 10, 100, 100, 100, 10, 0],
        [0, 10, 10, 10, 10, 10, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ],
}

@pytest.fixture(
    params=get_combinations(
        {
            "layer": [
                Layer(np.array(MAP["Binary"])),
                np.array(MAP["Binary"]),
                Layer(np.array(MAP["Non Binary"])),
                np.array(MAP["Non Binary"]),
            ],
            "alpha": [None, np.zeros((7, 7), dtype=int), np.ones((7, 7), dtype=int)],
            "thresholds": [None, (0, 1), (10, 100), (10, 1000)],
            "invert": [True, False],
            "mask_size": [3, 5],
            "as_array": [True, False],
        }, 25)
)
def data_distance(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_distance_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
