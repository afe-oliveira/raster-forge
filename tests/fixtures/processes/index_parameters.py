import numpy as np
import pytest

from rforge.lib.containers.layer import Layer

np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        {
            "N": Layer(np.random.randint(0, MAX, size=SIZE)),
            "R": Layer(np.random.randint(0, MAX, size=SIZE)),
            "G": Layer(np.random.randint(0, MAX, size=SIZE)),
            "B": Layer(np.random.randint(0, MAX, size=SIZE)),
        },
        {
            "N": np.random.randint(0, MAX, size=SIZE),
            "R": np.random.randint(0, MAX, size=SIZE),
            "G": np.random.randint(0, MAX, size=SIZE),
            "B": np.random.randint(0, MAX, size=SIZE),
        },
        {
            "N": Layer(np.random.rand(7, 7) * MAX),
            "R": Layer(np.random.rand(7, 7) * MAX),
            "G": Layer(np.random.rand(7, 7) * MAX),
            "B": Layer(np.random.rand(7, 7) * MAX),
        },
        {
            "N": np.random.rand(7, 7) * MAX,
            "R": np.random.rand(7, 7) * MAX,
            "G": np.random.rand(7, 7) * MAX,
            "B": np.random.rand(7, 7) * MAX,
        },
        {
            "N": Layer(np.random.randint(0, MAX, size=SIZE)),
            "R": np.random.randint(0, MAX, size=SIZE),
            "G": Layer(np.random.rand(7, 7) * MAX),
            "B": np.random.rand(7, 7) * MAX,
        },
    ]
)
def index_parameters(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        [
            {
                "N": np.full(SIZE, "N"),
                "R": np.full(SIZE, "R"),
                "G": np.full(SIZE, "G"),
                "B": np.full(SIZE, "B"),
            },
            TypeError,
        ]
    ]
)
def index_parameters_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
