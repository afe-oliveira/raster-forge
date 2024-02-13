import numpy as np
import pytest


@pytest.fixture(
    params=[
        {},
        {"array": np.random.rand(10, 10)},
        {"array": np.random.rand(10, 10, 2)},
        {"array": np.random.rand(10, 10, 3)},
        {
            "array": np.random.rand(10, 10),
            "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
        },
        {
            "array": np.random.rand(10, 10),
            "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
            "crs": "EPSG:3763",
        },
        {
            "array": np.random.rand(10, 10),
            "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
            "crs": "EPSG:3763",
            "driver": "PNG",
        },
        {
            "array": np.random.rand(10, 10),
            "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
            "crs": "EPSG:3763",
            "driver": "PNG",
            "no_data": -9999,
        },
        {
            "array": np.random.rand(10, 10),
            "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
            "crs": "EPSG:3763",
            "driver": "PNG",
            "no_data": -9999,
            "transform": (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        },
        {
            "array": np.random.rand(10, 10),
            "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
            "crs": "EPSG:3763",
            "driver": "PNG",
            "no_data": -9999,
            "transform": (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
            "units": "Meters",
        },
    ]
)
def data_layer_init(request):
    """Fixture that defines the layer initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        ({"array": np.random.rand(10, 10).astype(str)}, TypeError),
        ({"array": np.random.rand(10, 10, 2).astype(bool)}, TypeError),
        ({"array": np.random.rand(10, 10), "bounds": True}, TypeError),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10},
            },
            TypeError,
        ),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10, "bottom": "10"},
            },
            TypeError,
        ),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
                "crs": 1000,
            },
            TypeError,
        ),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
                "crs": "EPSG:3763",
                "driver": 1000,
            },
            TypeError,
        ),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
                "crs": "EPSG:3763",
                "driver": "PNG",
                "no_data": "-9999",
            },
            TypeError,
        ),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
                "crs": "EPSG:3763",
                "driver": "PNG",
                "no_data": -9999,
                "transform": ("1", 1.0, 1.0, 1.0, 1.0, "1"),
            },
            TypeError,
        ),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
                "crs": "EPSG:3763",
                "driver": "PNG",
                "no_data": -9999,
                "transform": (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
                "units": True,
            },
            TypeError,
        ),
        (
            {
                "array": np.random.rand(10, 10),
                "bounds": {"left": -10, "right": 10, "top": -10, "bottom": 10},
                "crs": "EPSG:3763",
                "driver": "PNG",
                "no_data": -9999,
                "transform": (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
                "units": 1000,
            },
            TypeError,
        ),
    ]
)
def data_layer_init_errors(request):
    """Fixture that defines the layer initialization data to be tested."""
    return request.param

