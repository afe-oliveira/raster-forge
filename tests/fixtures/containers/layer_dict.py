import numpy as np
import pytest

from rforge.containers.layer import Layer

np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        {
            "Layer 1": Layer(np.random.randint(0, MAX, size=SIZE)),
            "Layer 2": Layer(np.random.randint(0, MAX, size=SIZE)),
            "Layer 3": Layer(np.random.randint(0, MAX, size=SIZE)),
        },
        {
            "Layer 1": Layer(np.random.rand(7, 7) * MAX),
            "Layer 2": Layer(np.random.rand(7, 7) * MAX),
            "Layer 3": Layer(np.random.rand(7, 7) * MAX),
        },
        {
            "Layer 1": Layer(np.random.randint(0, MAX, size=SIZE)),
            "Layer 2": Layer(np.random.rand(7, 7) * MAX),
        },
        {},
    ]
)
def layer_dict(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[[], TypeError]])
def layer_dict_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=["Layer 1", "Layer 2", "Layer 3"])
def layer_dict_name(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=["Layer 4", "Layer 5", "Layer 6"])
def layer_dict_name_alt(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[1, TypeError], [10, TypeError]])
def layer_dict_name_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, MAX, size=SIZE)),
        Layer(np.random.rand(7, 7) * MAX),
    ]
)
def layer_dict_value(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        ["A", TypeError],
        [np.full(SIZE, "A"), TypeError],
    ]
)
def layer_dict_value_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
