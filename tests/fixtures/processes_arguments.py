import numpy as np
import pytest

from rforge.containers.layer import Layer

np.random.seed(42)

SIZE = (7, 7)
MAX = np.iinfo(np.int32).max

N = 5
LAYER_LISTS = []
for i in range(1, N + 1):
    LAYER_LISTS.append(
        [Layer(np.random.randint(0, MAX, size=SIZE)) for _ in range(0, i)]
    )
    LAYER_LISTS.append(
        [Layer(np.random.randint(0, MAX, size=SIZE)) for _ in range(0, i)]
    )
    LAYER_LISTS.append([np.random.randint(0, MAX, size=SIZE) for _ in range(0, i)])
    LAYER_LISTS.append([Layer(np.random.rand(7, 7) * MAX) for _ in range(0, i)])


@pytest.fixture(
    params=[
        Layer(np.random.randint(0, MAX, size=SIZE)),
        np.random.randint(0, MAX, size=SIZE),
        Layer(np.random.rand(7, 7) * MAX),
        np.random.rand(7, 7) * MAX,
    ]
)
def data_layer(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=LAYER_LISTS)
def data_layer_list(request):
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
def data_alpha(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[True, False])
def data_gamma(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[True, False])
def data_as_array(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[3, 5])
def data_mask_size(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
