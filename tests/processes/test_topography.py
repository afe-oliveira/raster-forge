import hashlib
import pickle

import numpy as np
import pytest
from rforge.processes.topography import aspect, slope

from tests.files.benchmarks.test_data import SLOPE_TEST_DATA, ASPECT_TEST_DATA

np.random.seed(42)

SLOPE_TEST_DATA.clear()
ASPECT_TEST_DATA.clear()

with open("tests/files/benchmarks/slope.pkl", "rb") as file:
    TESTS_SLOPE = pickle.load(file)

with open("tests/files/benchmarks/aspect.pkl", "rb") as file:
    TESTS_ASPECT = pickle.load(file)


def test_slope(layer, angle_units, alpha, as_array):
    """Test slope map creation function."""
    input_code = hashlib.sha256(
        pickle.dumps([layer, angle_units, alpha, as_array])
    ).hexdigest()
    result = TESTS_SLOPE.get(input_code, None)

    s = slope(dem=layer, units=angle_units, alpha=alpha, as_array=as_array)

    SLOPE_TEST_DATA.add(input_code, s)

    assert (as_array and np.allclose(s, result, atol=0.01)) or (
        not as_array and s == result
    )


def test_aspect(layer, angle_units, alpha, as_array):
    """Test aspect map creation function."""
    input_code = hashlib.sha256(
        pickle.dumps([layer, angle_units, alpha, as_array])
    ).hexdigest()
    result = TESTS_ASPECT.get(input_code, None)

    a = aspect(dem=layer, units=angle_units, alpha=alpha, as_array=as_array)

    ASPECT_TEST_DATA.add(input_code, a)

    assert (as_array and np.allclose(a, result, atol=0.01)) or (
        not as_array and a == result
    )


def test_dem_error(layer_error, angle_units, alpha, as_array):
    """Test slope map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        s = slope(
            dem=layer_error[0],
            units=angle_units,
            alpha=alpha,
            as_array=as_array,
        )
    with pytest.raises(layer_error[1]):
        a = aspect(
            dem=layer_error[0],
            units=angle_units,
            alpha=alpha,
            as_array=as_array,
        )


def test_angle_units_error(layer, angle_units_error, alpha, as_array):
    """Test slope map creation function for expected errors."""
    with pytest.raises(angle_units_error[1]):
        s = slope(
            dem=layer,
            units=angle_units_error[0],
            alpha=alpha,
            as_array=as_array,
        )
    with pytest.raises(angle_units_error[1]):
        a = aspect(
            dem=layer,
            units=angle_units_error[0],
            alpha=alpha,
            as_array=as_array,
        )


def test_alpha_error(layer, angle_units, alpha_error, as_array):
    """Test slope map creation function for expected errors."""
    with pytest.raises(alpha_error[1]):
        s = slope(
            dem=layer,
            units=angle_units,
            alpha=alpha_error[0],
            as_array=as_array,
        )
    with pytest.raises(alpha_error[1]):
        a = aspect(
            dem=layer,
            units=angle_units,
            alpha=alpha_error[0],
            as_array=as_array,
        )


def test_as_array_error(layer, angle_units, alpha, as_array_error):
    """Test slope map creation function for expected errors."""
    with pytest.raises(as_array_error[1]):
        s = slope(
            dem=layer,
            units=angle_units,
            alpha=alpha,
            as_array=as_array_error[0],
        )
    with pytest.raises(as_array_error[1]):
        a = aspect(
            dem=layer,
            units=angle_units,
            alpha=alpha,
            as_array=as_array_error[0],
        )
