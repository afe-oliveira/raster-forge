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
