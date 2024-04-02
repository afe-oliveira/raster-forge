import json

import numpy as np
import pytest
from rforge.library.containers.layer import Layer


def test_init(array, bounds, crs, driver, no_data, transform, layer_units):
    """Test Layer initialization function and variable setting."""
    l = Layer(
        array=array,
        bounds=bounds,
        crs=crs,
        driver=driver,
        transform=transform,
        no_data=no_data,
        units=layer_units,
    )

    assert isinstance(l, Layer)
    assert np.array_equal(l.array, array)
    assert l.bounds == bounds
    assert l.crs == crs
    assert l.driver == driver
    assert l.no_data == no_data
    assert l.transform == transform
    assert l.units == layer_units
    if l.array is not None:
        assert l.width == array.shape[1]
        assert l.height == array.shape[0]
        assert l.count == array.shape[2] if len(array.shape) > 2 else l.count == 1
        if transform is not None:
            assert l.resolution == transform[1]
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


def test_init_array_error(array_error):
    """Test layer initialization function for expected errors."""
    with pytest.raises(array_error[1]):
        Layer(
            array=array_error[0],
        )


def test_init_bounds_error(bounds_error):
    """Test layer initialization function for expected errors."""
    with pytest.raises(bounds_error[1]):
        Layer(
            bounds=bounds_error[0],
        )


def test_init_crs_error(crs_error):
    """Test layer initialization function for expected errors."""
    with pytest.raises(crs_error[1]):
        Layer(
            crs=crs_error[0],
        )


def test_init_driver_error(driver_error):
    """Test layer initialization function for expected errors."""
    with pytest.raises(driver_error[1]):
        Layer(
            driver=driver_error[0],
        )


def test_init_no_data_error(no_data_error):
    """Test layer initialization function for expected errors."""
    with pytest.raises(no_data_error[1]):
        Layer(
            no_data=no_data_error[0],
        )


def test_init_transform_error(transform_error):
    """Test layer initialization function for expected errors."""
    with pytest.raises(transform_error[1]):
        Layer(
            transform=transform_error[0],
        )


def test_init_layer_units_error(layer_units_error):
    """Test layer initialization function for expected errors."""
    with pytest.raises(layer_units_error[1]):
        Layer(
            units=layer_units_error[0],
        )


def test_setter(array, bounds, crs, driver, no_data, transform, layer_units):
    """Test Layer initialization function and variable setting."""
    l = Layer()
    l.array = array
    l.bounds = bounds
    l.crs = crs
    l.driver = driver
    l.no_data = no_data
    l.transform = transform
    l.units = layer_units

    assert isinstance(l, Layer)
    assert np.array_equal(l.array, array)
    assert l.bounds == bounds
    assert l.crs == crs
    assert l.driver == driver
    assert l.no_data == no_data
    assert l.transform == transform
    assert l.units == layer_units
    if l.array is not None:
        assert l.width == array.shape[1]
        assert l.height == array.shape[0]
        assert l.count == array.shape[2] if len(array.shape) > 2 else l.count == 1
        if transform is not None:
            assert l.resolution == transform[1]
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


def test_setter_array_error(array_error):
    """Test layer initialization function for expected errors."""
    l = Layer()
    with pytest.raises(array_error[1]):
        l.array = array_error[0]


def test_setter_bounds_error(bounds_error):
    """Test layer initialization function for expected errors."""
    l = Layer()
    with pytest.raises(bounds_error[1]):
        l.bounds = bounds_error[0]


def test_setter_crs_error(crs_error):
    """Test layer initialization function for expected errors."""
    l = Layer()
    with pytest.raises(crs_error[1]):
        l.crs = crs_error[0]


def test_setter_driver_error(driver_error):
    """Test layer initialization function for expected errors."""
    l = Layer()
    with pytest.raises(driver_error[1]):
        l.driver = driver_error[0]


def test_setter_no_data_error(no_data_error):
    """Test layer initialization function for expected errors."""
    l = Layer()
    with pytest.raises(no_data_error[1]):
        l.no_data = no_data_error[0]


def test_setter_transform_error(transform_error):
    """Test layer initialization function for expected errors."""
    l = Layer()
    with pytest.raises(transform_error[1]):
        l.transform = transform_error[0]


def test_setter_layer_units_error(layer_units_error):
    """Test layer initialization function for expected errors."""
    l = Layer()
    with pytest.raises(layer_units_error[1]):
        l.units = layer_units_error[0]


def test_import(data_import):
    """Test Layer import function."""
    data_path = data_import.get("data_path", None)
    info_path = data_import.get("info_path", None)
    scale = data_import.get("scale", None)

    with open(info_path, "r") as json_file:
        info = json.load(json_file)

    for i in range(1, info["band_num"] + 1):
        l = Layer()
        info_aux = info[f"Layer {i}"]
        l.import_layer(data_path, i, scale)

        assert np.array_equal(l.array, info_aux["array"])
        assert l.bounds == info_aux["bounds"]
        assert l.crs == info_aux["crs"]
        assert l.driver == info_aux["driver"]
        assert l.no_data == info_aux["no_data"]
        assert l.resolution == info_aux["resolution"]
        assert l.transform == tuple(info_aux["transform"])
        assert l.units == info_aux["units"]
        assert l.height == info_aux["height"]
        assert l.width == info_aux["width"]
        assert l.mean == info_aux["mean"]
        assert l.median == info_aux["median"]
        assert l.min == info_aux["minimum"]
        assert l.max == info_aux["maximum"]
        assert l.std_dev == info_aux["standard_deviation"]


def test_import_error(data_import_error):
    """Test Layer import function."""
    data_path = data_import_error.get("data_path", None)
    error = data_import_error.get("error", None)
    scale = data_import_error.get("scale", None)

    with pytest.raises(error):
        l = Layer()
        l.import_layer(data_path, 1, scale)
