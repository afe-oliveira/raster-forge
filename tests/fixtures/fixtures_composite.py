import pickle
import random

import numpy as np
import pytest

from rforge.containers.layer import Layer

with open("tests/files/composite.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_composite(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {
            "layers": [
                np.array(["A", "A", "A"]),
                np.array(["B", "B", "B"]),
                np.array(["C", "C", "C"]),
            ],
            "alpha": np.ones(3, dtype=int),
            "gamma": [1.0, 1.0, 1.0],
            "as_array": False,
            "error": TypeError,
        },
        {
            "layers": [Layer(np.random.randint(0, 25000, size=3)) for _ in range(3)],
            "alpha": np.array(["D", "D", "D"]),
            "gamma": [1.0, 1.0, 1.0],
            "as_array": False,
            "error": TypeError,
        },
        {
            "layers": [Layer(np.random.randint(0, 25000, size=3)) for _ in range(3)],
            "alpha": np.array(["D", "D", "D"]),
            "gamma": [1.0, 1.0],
            "as_array": False,
            "error": TypeError,
        },
        {
            "layers": [Layer(np.random.randint(0, 25000, size=3)) for _ in range(3)],
            "alpha": np.ones(3, dtype=int),
            "gamma": ["1.0", "1.0", "1.0"],
            "as_array": False,
            "error": TypeError,
        },
        {
            "layers": [Layer(np.random.randint(0, 25000, size=3)) for _ in range(3)],
            "alpha": np.ones(3, dtype=int),
            "gamma": [1.0, 1.0, 1.0],
            "as_array": "False",
            "error": TypeError,
        },
    ]
)
def data_composite_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
