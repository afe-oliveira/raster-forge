import pickle

import numpy as np
import pytest

from rforge.containers.layer import Layer

with open("tests/files/distance.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_distance(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {
            "layer": np.array(["A", "A", "A"]),
            "alpha": np.ones(3, dtype=int),
            "thresholds": (20, 80),
            "invert": False,
            "mask_size": 3,
            "as_array": False,
            "error": TypeError,
        },
        {
            "layer": Layer(np.random.randint(0, 100, size=3)),
            "alpha": np.array(["D", "D", "D"]),
            "thresholds": (20, 80),
            "invert": False,
            "mask_size": 3,
            "as_array": False,
            "error": TypeError,
        },
        {
            "layer": Layer(np.random.randint(0, 100, size=3)),
            "alpha": np.ones(3, dtype=int),
            "thresholds": ("20", "80"),
            "invert": False,
            "mask_size": 3,
            "as_array": False,
            "error": TypeError,
        },
        {
            "layer": Layer(np.random.randint(0, 100, size=3)),
            "alpha": np.ones(3, dtype=int),
            "thresholds": (20, 80),
            "invert": "False",
            "mask_size": 3,
            "as_array": False,
            "error": TypeError,
        },
        {
            "layer": Layer(np.random.randint(0, 100, size=3)),
            "alpha": np.ones(3, dtype=int),
            "thresholds": (20, 80),
            "invert": False,
            "mask_size": "3",
            "as_array": False,
            "error": TypeError,
        },
        {
            "layer": Layer(np.random.randint(0, 100, size=3)),
            "alpha": np.ones(3, dtype=int),
            "thresholds": (20, 80),
            "invert": False,
            "mask_size": 4,
            "as_array": False,
            "error": TypeError,
        },
        {
            "layer": Layer(np.random.randint(0, 100, size=3)),
            "alpha": np.ones(3, dtype=int),
            "thresholds": (20, 80),
            "invert": False,
            "mask_size": 3,
            "as_array": "False",
            "error": TypeError,
        },
    ]
)
def data_distance_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
