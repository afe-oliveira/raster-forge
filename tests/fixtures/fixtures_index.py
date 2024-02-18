import pickle

import numpy as np
import pytest

from rforge.containers.layer import Layer

with open("benchmarks/files/index.pkl", "rb") as file:
    parameters = pickle.load(file)


@pytest.fixture(params=parameters)
def data_index(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {
            "index_id": "NDVI",
            "parameters": {
                "N": np.array(["A", "A", "A"]),
                "R": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "G": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "B": Layer(np.random.randint(0, 25500, size=(7, 7))),
            },
            "alpha": np.ones((7, 7), dtype=int),
            "thresholds": (100, 10000),
            "binarize": False,
            "as_array": False,
            "error": TypeError,
        },
        {
            "index_id": "NDVI",
            "parameters": {
                "N": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "R": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "G": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "B": Layer(np.random.randint(0, 25500, size=(7, 7))),
            },
            "alpha": np.array(["D", "D", "D"]),
            "thresholds": (100, 10000),
            "binarize": False,
            "as_array": False,
            "error": TypeError,
        },
        {
            "index_id": "NDVI",
            "parameters": {
                "N": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "R": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "G": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "B": Layer(np.random.randint(0, 25500, size=(7, 7))),
            },
            "alpha": np.ones((7, 7), dtype=int),
            "thresholds": ("100", 10000),
            "binarize": False,
            "as_array": False,
            "error": TypeError,
        },
        {
            "index_id": "NDVI",
            "parameters": {
                "N": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "R": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "G": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "B": Layer(np.random.randint(0, 25500, size=(7, 7))),
            },
            "alpha": np.ones((7, 7), dtype=int),
            "thresholds": (100, 10000),
            "binarize": "False",
            "as_array": False,
            "error": TypeError,
        },
        {
            "index_id": "NDVI",
            "parameters": {
                "N": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "R": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "G": Layer(np.random.randint(0, 25500, size=(7, 7))),
                "B": Layer(np.random.randint(0, 25500, size=(7, 7))),
            },
            "alpha": np.ones((7, 7), dtype=int),
            "thresholds": (100, 10000),
            "binarize": False,
            "as_array": "False",
            "error": TypeError,
        },
    ]
)
def data_index_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
