import numpy as np
import pytest

from rforge.containers.layer import Layer

MIN = 0
MAX = 25000
SHAPE = (5, 5)


@pytest.fixture(params=[])
def data_composite(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(params=[])
def data_composite_error(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
