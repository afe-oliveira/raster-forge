import numpy as np
import pytest

np.random.seed(42)


@pytest.fixture(
    params=[
        (
            np.random.randint(210, 219),
            np.random.randint(220, 229),
            np.random.randint(230, 239),
        )
    ]
)
def fuel_models(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        [
            (
                np.random.uniform(210.0, 219.0),
                np.random.uniform(220.0, 229.0),
                np.random.uniform(230.0, 239.0),
            ),
            TypeError,
        ],
        [
            (
                str(np.random.uniform(210.0, 219.0)),
                str(np.random.uniform(220.0, 229.0)),
                str(np.random.uniform(230.0, 239.0)),
            ),
            TypeError,
        ],
    ]
)
def fuel_models_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
