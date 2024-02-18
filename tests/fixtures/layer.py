import numpy as np
import pytest

from rforge.containers.layer import Layer

np.random.seed(42)


SIZE = (7, 7)
MAX = np.iinfo(np.int32).max


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, MAX, size=SIZE)),
        np.random.randint(0, MAX, size=SIZE),
        Layer(np.random.rand(7, 7) * MAX),
        np.random.rand(7, 7) * MAX,
    ]
)
def layer(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, 100, size=SIZE)),
        np.random.randint(0, 100, size=SIZE),
        Layer(np.random.rand(7, 7) * 100),
        np.random.rand(7, 7) * 100,
    ]
)
def coverage(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, 6, size=SIZE)),
        np.random.randint(0, 6, size=SIZE),
    ]
)
def distance(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, 150, size=SIZE)),
        np.random.randint(0, 150, size=SIZE),
        Layer(np.random.rand(7, 7) * 150),
        np.random.rand(7, 7) * 150,
    ]
)
def height(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, 1, size=SIZE)),
        np.random.randint(0, 1, size=SIZE),
    ]
)
def water(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, 1, size=SIZE)),
        np.random.randint(0, 1, size=SIZE),
    ]
)
def artificial(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, MAX, size=SIZE)),
        np.random.randint(0, MAX, size=SIZE),
        Layer(np.random.rand(7, 7) * MAX),
        np.random.rand(7, 7) * MAX,
    ]
)
def dsm(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, MAX, size=SIZE)),
        np.random.randint(0, MAX, size=SIZE),
        Layer(np.random.rand(7, 7) * MAX),
        np.random.rand(7, 7) * MAX,
    ]
)
def dtm(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[[np.full(SIZE, "A"), TypeError]])
def layer_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
