import numpy as np
import pytest


@pytest.fixture(
    params=list(
        np.concatenate(
            (
                np.random.randint(low=0, high=25, size=10),
                np.random.uniform(low=0.0, high=25.0, size=10),
            )
        )
    )
)
def tree_height(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[["A", TypeError]])
def tree_height_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
