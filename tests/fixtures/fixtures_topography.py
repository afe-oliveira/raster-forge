import pickle

import numpy as np
import pytest

from rforge.containers.layer import Layer

with open("tests/files/topography.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_topography(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {
            "dem": np.array(["A", "A", "A"]),
            "units": "degrees",
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "dem": Layer(np.random.rand(7, 7) * 10000),
            "units": "AAAA",
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "dem": Layer(np.random.rand(7, 7) * 10000),
            "units": 10.0,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "dem": Layer(np.random.rand(7, 7) * 10000),
            "units": "degrees",
            "alpha": np.array(["D", "D", "D"]),
            "as_array": False,
            "error": TypeError,
        },
        {
            "dem": Layer(np.random.rand(7, 7) * 10000),
            "units": "degrees",
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": "False",
            "error": TypeError,
        },
    ]
)
def data_topography_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
