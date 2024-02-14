import pickle

import numpy as np
import pytest

from rforge.containers.layer import Layer

with open("tests/files/fuel.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_fuel(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {
            "coverage": np.array(["A", "A", "A"]),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, 220, 230),
            "tree_height": 1,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": np.array(["A", "A", "A"]),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, 220, 230),
            "tree_height": 1,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": np.array(["A", "A", "A"]),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, 220, 230),
            "tree_height": 1,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": np.array(["A", "A", "A"]),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, 220, 230),
            "tree_height": 1,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": np.array(["A", "A", "A"]),
            "models": (210, 220, 230),
            "tree_height": 1,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, "220", 230),
            "tree_height": 1,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, 220, 230),
            "tree_height": "1",
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, 220, 230),
            "tree_height": 1,
            "alpha": np.array(["A", "A", "A"]),
            "as_array": False,
            "error": TypeError,
        },
        {
            "coverage": Layer(np.random.rand(7, 7) * 100),
            "height": Layer(np.random.rand(7, 7) * 100),
            "distance": Layer(np.random.randint(0, 7, size=(7, 7))),
            "water": Layer(np.random.randint(0, 1, size=(7, 7))),
            "artificial": Layer(np.random.randint(0, 1, size=(7, 7))),
            "models": (210, 220, 230),
            "tree_height": 1,
            "alpha": np.ones((7, 7), dtype=int),
            "as_array": "False",
            "error": TypeError,
        },
    ]
)
def data_fuel_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
