import numpy as np
import pytest

from rforge.containers.layer import Layer


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


@pytest.fixture(
    params=[
        {
            "path": "tests\\files\\cea.tif",
            "id": 1,
            "crs": "4326",
            "driver": "GTIFF",
            "bounds": {
                "left": -28493.166784412522,
                "bottom": 4224973.143255847,
                "right": 2358.211624949061,
                "top": 4255884.5438021915,
            },
            "no_data": None,
            "transform": (
                -28493.166784412522,
                60.02213698319374,
                0.0,
                4255884.5438021915,
                0.0,
                -60.02213698319374,
            ),
            "units": None,
            "width": 514,
            "height": 515,
            "count": 1,
            "mean": 103.14948811907371,
            "median": 99.0,
            "minimum": 0,
            "maximum": 255,
            "standard_deviation": 58.897344713758585,
        },
        {
            "path": "tests\\files\\geos.tif",
            "id": 1,
            "crs": "4326",
            "driver": "GTIFF",
            "bounds": {
                "left": 8.999654601821101,
                "bottom": 51.9999732301211,
                "right": 9.0024601573789,
                "top": 52.0027787856789,
            },
            "no_data": None,
            "transform": (
                8.999654601821101,
                2.77777778e-05,
                0.0,
                52.0027787856789,
                0.0,
                -2.77777778e-05,
            ),
            "units": None,
            "width": 101,
            "height": 101,
            "count": 1,
            "mean": 1.796588569748064,
            "median": 2.0,
            "minimum": 0,
            "maximum": 2,
            "standard_deviation": 0.6044407505635215,
        },
        {
            "path": "tests\\files\\bogota.tif",
            "id": 1,
            "crs": "21897",
            "driver": "GTIFF",
            "bounds": {
                "left": 440720.0,
                "bottom": 69280.0,
                "right": 471440.0,
                "top": 100000.0,
            },
            "no_data": None,
            "transform": (440720.0, 60.0, 0.0, 100000.0, 0.0, -60.0),
            "units": None,
            "width": 512,
            "height": 512,
            "count": 1,
            "mean": 104.13526916503906,
            "median": 99.0,
            "minimum": 0,
            "maximum": 255,
            "standard_deviation": 58.30845522919804,
        },
    ]
)
def data_layer_import(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {"scale": 1, "layers": 0},
        {"scale": 1, "layers": 1},
        {"scale": 1, "layers": 10},
        {"scale": 10, "layers": 0},
        {"scale": 10, "layers": 1},
        {"scale": 10, "layers": 10},
    ]
)
def data_raster_init(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {"scale": 1, "layers": []},
        {"scale": 1, "layers": [Layer() for _ in range(1)]},
        {"scale": 1, "layers": [Layer() for _ in range(10)]},
        {"scale": 10, "layers": []},
        {"scale": 10, "layers": [Layer() for _ in range(1)]},
        {"scale": 10, "layers": [Layer() for _ in range(10)]},
    ]
)
def data_raster_init(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param
