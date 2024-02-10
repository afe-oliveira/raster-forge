import json

import numpy as np
import pytest

from rforge.containers.layer import Layer


def test_init(data_layer_init):
    """Test Layer initialization function and variable setting."""
    array = data_layer_init.get("array", None)
    bounds = data_layer_init.get("bounds", None)
    crs = data_layer_init.get("crs", None)
    driver = data_layer_init.get("driver", None)
    no_data = data_layer_init.get("no_data", None)
    transform = data_layer_init.get("transform", None)
    units = data_layer_init.get("units", None)

    l = Layer(
        array=array,
        bounds=bounds,
        crs=crs,
        driver=driver,
        transform=transform,
        no_data=no_data,
        units=units,
    )

    assert isinstance(l, Layer)
    assert np.array_equal(l.array, array)
    assert l.bounds == bounds
    assert l.crs == crs
    assert l.driver == driver
    assert l.no_data == no_data
    assert l.transform == transform
    assert l.units == units
    if l.array is not None:
        assert l.width == array.shape[1]
        assert l.height == array.shape[0]
        assert l.count == array.shape[2] if len(array.shape) > 2 else l.count == 1
        if transform is not None:
            assert l.resolution == transform[2]
        assert (
            np.array_equal(l.mean, np.mean(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.mean, [np.mean(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.median, np.median(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.median, [np.median(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.min, np.min(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.min, [np.min(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.max, np.max(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.max, [np.max(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.std_dev, np.std(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.std_dev, [np.std(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )


def test_init_setter(data_layer_init):
    """Test Layer initialization function and variable setting."""
    array = data_layer_init.get("array", None)
    bounds = data_layer_init.get("bounds", None)
    crs = data_layer_init.get("crs", None)
    driver = data_layer_init.get("driver", None)
    no_data = data_layer_init.get("no_data", None)
    transform = data_layer_init.get("transform", None)
    units = data_layer_init.get("units", None)

    l = Layer()
    l.array = array
    l.bounds = bounds
    l.crs = crs
    l.driver = driver
    l.no_data = no_data
    l.transform = transform
    l.units = units

    assert isinstance(l, Layer)
    assert np.array_equal(l.array, array)
    assert l.bounds == bounds
    assert l.crs == crs
    assert l.driver == driver
    assert l.no_data == no_data
    assert l.transform == transform
    assert l.units == units
    if l.array is not None:
        assert l.width == array.shape[1]
        assert l.height == array.shape[0]
        assert l.count == array.shape[2] if len(array.shape) > 2 else l.count == 1
        if transform is not None:
            assert l.resolution == transform[2]
        assert (
            np.array_equal(l.mean, np.mean(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.mean, [np.mean(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.median, np.median(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.median, [np.median(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.min, np.min(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.min, [np.min(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.max, np.max(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.max, [np.max(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )
        assert (
            np.array_equal(l.std_dev, np.std(array))
            if len(array.shape) <= 2
            else (
                np.array_equal(
                    l.std_dev, [np.std(array[:, :, i]) for i in range(array.shape[2])]
                )
            )
        )


def test_init_import(data_import):
    """Test Layer import function."""
    data_path = data_import.get("data_path", None)
    info_path = data_import.get("info_path", None)
    scale = data_import.get("scale", None)

    with open(info_path, 'r') as json_file:
        info = json.load(json_file)

    for i in range(1, info['band_num'] + 1):
        l = Layer()
        info_aux = info[f"Layer {i}"]
        l.import_layer(data_path, i, scale)

        assert np.array_equal(l.array, info_aux['array'])
        assert l.bounds == info_aux['bounds']
        assert l.crs == info_aux['crs']
        assert l.driver == info_aux['driver']
        assert l.no_data == info_aux['no_data']
        assert l.resolution == info_aux['resolution']
        assert l.transform == tuple(info_aux['transform'])
        assert l.units == info_aux['units']
        assert l.height == info_aux['height']
        assert l.width == info_aux['width']
        assert l.mean == info_aux['mean']
        assert l.median == info_aux['median']
        assert l.min == info_aux['minimum']
        assert l.max == info_aux['maximum']
        assert l.std_dev == info_aux['standard_deviation']


def test_init_errors(data_layer_init_errors):
    """Test layer initialization function for expected errors."""
    array = data_layer_init_errors[0].get("array", None)
    bounds = data_layer_init_errors[0].get("bounds", None)
    crs = data_layer_init_errors[0].get("crs", None)
    driver = data_layer_init_errors[0].get("driver", None)
    no_data = data_layer_init_errors[0].get("no_data", None)
    transform = data_layer_init_errors[0].get("transform", None)
    units = data_layer_init_errors[0].get("units", None)

    with pytest.raises(data_layer_init_errors[1]):
        Layer(
            array=array,
            bounds=bounds,
            crs=crs,
            driver=driver,
            transform=transform,
            no_data=no_data,
            units=units,
        )


def test_init_setter_errors(data_layer_init_errors):
    """Test Layer initialization function and variable setting for expected errors."""
    array = data_layer_init_errors[0].get("array", None)
    bounds = data_layer_init_errors[0].get("bounds", None)
    crs = data_layer_init_errors[0].get("crs", None)
    driver = data_layer_init_errors[0].get("driver", None)
    no_data = data_layer_init_errors[0].get("no_data", None)
    transform = data_layer_init_errors[0].get("transform", None)
    units = data_layer_init_errors[0].get("units", None)

    l = Layer()

    with pytest.raises(data_layer_init_errors[1]):
        l.array = array
        l.bounds = bounds
        l.crs = crs
        l.driver = driver
        l.no_data = no_data
        l.transform = transform
        l.units = units


def test_init_import_errors(data_import_errors):
    """Test Layer import function."""
    data_path = data_import_errors.get("data_path", None)
    error = data_import_errors.get("error", None)
    scale = data_import_errors.get("scale", None)

    with pytest.raises(error):
        l = Layer()
        l.import_layer(data_path, 1, scale)