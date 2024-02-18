import pickle

import numpy as np
import pytest

from rforge.containers.layer import Layer

with open("benchmarks/files/height.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_height(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {
            "dsm": np.array(["A", "A", "A"]),
            "dtm": Layer(np.random.rand(7, 7) * 10000),
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "dsm": Layer(np.random.rand(7, 7) * 10000),
            "dtm": np.array(["A", "A", "A"]),
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "dsm": Layer(np.random.rand(7, 7) * 10000),
            "dtm": Layer(np.random.rand(7, 7) * 10000),
            "alpha": np.array(["D", "D", "D"]),
            "as_array": False,
            "error": TypeError,
        },
        {
            "dsm": Layer(np.random.rand(7, 7) * 10000),
            "dtm": Layer(np.random.rand(7, 7) * 10000),
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": "False",
            "error": TypeError,
        },
    ]
)
def data_height_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
