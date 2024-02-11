import random

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
        {"scale": 1, "layers": {}},
        {"scale": 1, "layers": {'Layer 1': Layer()}},
        {"scale": 1, "layers": {'Layer 1': Layer(), 'Layer 2': Layer(), 'Layer 3': Layer(), 'Layer 4': Layer(), 'Layer 5': Layer()}},
        {"scale": 10, "layers": {}},
        {"scale": 10, "layers": {'Layer 1': Layer()}},
        {"scale": 10, "layers": {'Layer 1': Layer(), 'Layer 2': Layer(), 'Layer 3': Layer(), 'Layer 4': Layer(), 'Layer 5': Layer()}},
    ]
)
def data_raster_init(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {"scale": '1', "layers": {}, 'error': TypeError},
        {"scale": None, "layers": {}, 'error': TypeError},
        {"scale": [], "layers": {}, 'error': TypeError},
        {"scale": 1, "layers": {'Layer 1': 'Layer'}, 'error': TypeError},
        {"scale": 1, "layers": {1: Layer()}, 'error': TypeError},
        {"scale": 1, "layers": {'Layer 1': Layer(), 'Layer 2': 'Layer'}, 'error': TypeError},
        {"scale": 1, "layers": {'Layer 1': Layer(), 2: Layer()}, 'error': TypeError}
    ]
)
def data_raster_init_errors(request):
    """Fixture that defines the raster initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {'data_path': 'tests/files/samples/ADSM_1.tif', 'info_path': 'tests/files/information/ADSM_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADSM_2.tif', 'info_path': 'tests/files/information/ADSM_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADSM_3.tif', 'info_path': 'tests/files/information/ADSM_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADSM_4.tif', 'info_path': 'tests/files/information/ADSM_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADSM_5.tif', 'info_path': 'tests/files/information/ADSM_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADTM_1.tif', 'info_path': 'tests/files/information/ADTM_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADTM_2.tif', 'info_path': 'tests/files/information/ADTM_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADTM_3.tif', 'info_path': 'tests/files/information/ADTM_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADTM_4.tif', 'info_path': 'tests/files/information/ADTM_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/ADTM_5.tif', 'info_path': 'tests/files/information/ADTM_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_1.tif', 'info_path': 'tests/files/information/AO_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_2.tif', 'info_path': 'tests/files/information/AO_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_3.tif', 'info_path': 'tests/files/information/AO_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_4.tif', 'info_path': 'tests/files/information/AO_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_5.tif', 'info_path': 'tests/files/information/AO_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_6.tif', 'info_path': 'tests/files/information/AO_6.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_7.tif', 'info_path': 'tests/files/information/AO_7.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_8.tif', 'info_path': 'tests/files/information/AO_8.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_9.tif', 'info_path': 'tests/files/information/AO_9.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_10.tif', 'info_path': 'tests/files/information/AO_10.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_11.tif', 'info_path': 'tests/files/information/AO_11.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_12.tif', 'info_path': 'tests/files/information/AO_12.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_13.tif', 'info_path': 'tests/files/information/AO_13.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_14.tif', 'info_path': 'tests/files/information/AO_14.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_15.tif', 'info_path': 'tests/files/information/AO_15.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_16.tif', 'info_path': 'tests/files/information/AO_16.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_17.tif', 'info_path': 'tests/files/information/AO_17.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_18.tif', 'info_path': 'tests/files/information/AO_18.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_19.tif', 'info_path': 'tests/files/information/AO_19.json', 'scale': 1},
        {'data_path': 'tests/files/samples/AO_20.tif', 'info_path': 'tests/files/information/AO_20.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDSM_1.tif', 'info_path': 'tests/files/information/SDSM_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDSM_2.tif', 'info_path': 'tests/files/information/SDSM_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDSM_3.tif', 'info_path': 'tests/files/information/SDSM_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDSM_4.tif', 'info_path': 'tests/files/information/SDSM_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDSM_5.tif', 'info_path': 'tests/files/information/SDSM_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDTM_1.tif', 'info_path': 'tests/files/information/SDTM_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDTM_2.tif', 'info_path': 'tests/files/information/SDTM_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDTM_3.tif', 'info_path': 'tests/files/information/SDTM_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDTM_4.tif', 'info_path': 'tests/files/information/SDTM_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SDTM_5.tif', 'info_path': 'tests/files/information/SDTM_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_1.tif', 'info_path': 'tests/files/information/SO_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_2.tif', 'info_path': 'tests/files/information/SO_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_3.tif', 'info_path': 'tests/files/information/SO_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_4.tif', 'info_path': 'tests/files/information/SO_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_5.tif', 'info_path': 'tests/files/information/SO_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_6.tif', 'info_path': 'tests/files/information/SO_6.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_7.tif', 'info_path': 'tests/files/information/SO_7.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_8.tif', 'info_path': 'tests/files/information/SO_8.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_9.tif', 'info_path': 'tests/files/information/SO_9.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_10.tif', 'info_path': 'tests/files/information/SO_10.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_11.tif', 'info_path': 'tests/files/information/SO_11.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_12.tif', 'info_path': 'tests/files/information/SO_12.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_13.tif', 'info_path': 'tests/files/information/SO_13.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_14.tif', 'info_path': 'tests/files/information/SO_14.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_15.tif', 'info_path': 'tests/files/information/SO_15.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_16.tif', 'info_path': 'tests/files/information/SO_16.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_17.tif', 'info_path': 'tests/files/information/SO_17.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_18.tif', 'info_path': 'tests/files/information/SO_18.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_19.tif', 'info_path': 'tests/files/information/SO_19.json', 'scale': 1},
        {'data_path': 'tests/files/samples/SO_20.tif', 'info_path': 'tests/files/information/SO_20.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDSM_1.tif', 'info_path': 'tests/files/information/TDSM_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDSM_2.tif', 'info_path': 'tests/files/information/TDSM_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDSM_3.tif', 'info_path': 'tests/files/information/TDSM_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDSM_4.tif', 'info_path': 'tests/files/information/TDSM_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDSM_5.tif', 'info_path': 'tests/files/information/TDSM_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDTM_1.tif', 'info_path': 'tests/files/information/TDTM_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDTM_2.tif', 'info_path': 'tests/files/information/TDTM_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDTM_3.tif', 'info_path': 'tests/files/information/TDTM_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDTM_4.tif', 'info_path': 'tests/files/information/TDTM_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TDTM_5.tif', 'info_path': 'tests/files/information/TDTM_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_1.tif', 'info_path': 'tests/files/information/TO_1.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_2.tif', 'info_path': 'tests/files/information/TO_2.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_3.tif', 'info_path': 'tests/files/information/TO_3.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_4.tif', 'info_path': 'tests/files/information/TO_4.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_5.tif', 'info_path': 'tests/files/information/TO_5.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_6.tif', 'info_path': 'tests/files/information/TO_6.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_7.tif', 'info_path': 'tests/files/information/TO_7.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_8.tif', 'info_path': 'tests/files/information/TO_8.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_9.tif', 'info_path': 'tests/files/information/TO_9.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_10.tif', 'info_path': 'tests/files/information/TO_10.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_11.tif', 'info_path': 'tests/files/information/TO_11.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_12.tif', 'info_path': 'tests/files/information/TO_12.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_13.tif', 'info_path': 'tests/files/information/TO_13.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_14.tif', 'info_path': 'tests/files/information/TO_14.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_15.tif', 'info_path': 'tests/files/information/TO_15.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_16.tif', 'info_path': 'tests/files/information/TO_16.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_17.tif', 'info_path': 'tests/files/information/TO_17.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_18.tif', 'info_path': 'tests/files/information/TO_18.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_19.tif', 'info_path': 'tests/files/information/TO_19.json', 'scale': 1},
        {'data_path': 'tests/files/samples/TO_20.tif', 'info_path': 'tests/files/information/TO_20.json', 'scale': 1}
    ]
)
def data_import(request):
    """Fixture that defines the layer initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {'data_path': 'tests/files/samples/AAAA.tif', 'error': FileNotFoundError, 'scale': 1},
        {'data_path': 'tests/files/samples/BBBB.tif', 'error': FileNotFoundError, 'scale': 1},
        {'data_path': 'tests/files/samples/CCCC.tif', 'error': FileNotFoundError, 'scale': 1},
        {'data_path': 'tests/files/samples/DDDD.tif', 'error': FileNotFoundError, 'scale': 1},
        {'data_path': 'tests/files/samples/EEEE.tif', 'error': FileNotFoundError, 'scale': 1}
    ]
)
def data_import_errors(request):
    """Fixture that defines the layer initialization data to be tested."""
    return request.param