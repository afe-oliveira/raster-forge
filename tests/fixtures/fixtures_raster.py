import pytest

from rforge.containers.layer import Layer


@pytest.fixture(
    params=[
        {"scale": 1, "layers": {}},
        {"scale": 1, "layers": {"Layer 1": Layer()}},
        {
            "scale": 1,
            "layers": {
                "Layer 1": Layer(),
                "Layer 2": Layer(),
                "Layer 3": Layer(),
                "Layer 4": Layer(),
                "Layer 5": Layer(),
            },
        },
        {"scale": 10, "layers": {}},
        {"scale": 10, "layers": {"Layer 1": Layer()}},
        {
            "scale": 10,
            "layers": {
                "Layer 1": Layer(),
                "Layer 2": Layer(),
                "Layer 3": Layer(),
                "Layer 4": Layer(),
                "Layer 5": Layer(),
            },
        },
    ]
)
def data_raster_init(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {"scale": "1", "layers": {}, "error": TypeError},
        {"scale": None, "layers": {}, "error": TypeError},
        {"scale": [], "layers": {}, "error": TypeError},
        {"scale": 1, "layers": ["Layer 1"], "error": TypeError},
        {"scale": 1, "layers": {"Layer 1": "Layer"}, "error": TypeError},
        {"scale": 1, "layers": {1: Layer()}, "error": TypeError},
        {
            "scale": 1,
            "layers": {"Layer 1": Layer(), "Layer 2": "Layer"},
            "error": TypeError,
        },
        {"scale": 1, "layers": {"Layer 1": Layer(), 2: Layer()}, "error": TypeError},
    ]
)
def data_raster_init_errors(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param