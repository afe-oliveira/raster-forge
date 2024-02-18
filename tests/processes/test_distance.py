import hashlib
import pickle

import numpy as np
import pytest
from rforge.processes.distance import distance

from tests.files.benchmarks.test_data import DISTANCE_TEST_DATA

np.random.seed(42)

DISTANCE_TEST_DATA.clear()

with open("tests/files/benchmarks/distance.pkl", "rb") as file:
    TESTS = pickle.load(file)


def test(layer, alpha, thresholds, invert, mask_size, as_array):
    """Test distance field creation function."""
    input_code = hashlib.sha256(
        pickle.dumps(
            [
                layer,
                alpha,
                thresholds,
                invert,
                mask_size,
                as_array,
            ]
        )
    ).hexdigest()
    result = TESTS.get(input_code, None)

    d = distance(
        layer=layer,
        alpha=alpha,
        thresholds=thresholds,
        invert=invert,
        mask_size=mask_size,
        as_array=as_array,
    )

    DISTANCE_TEST_DATA.add(input_code, d)

    assert (as_array and np.allclose(d, result, atol=0.01)) or (
        not as_array and d == result
    )


def test_layer_errors(layer_error, alpha, thresholds, invert, mask_size, as_array):
    """Test distance field creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        d = distance(
            layer=layer_error[0],
            alpha=alpha,
            thresholds=thresholds,
            invert=invert,
            mask_size=mask_size,
            as_array=as_array,
        )


def test_alpha_errors(layer, alpha_error, thresholds, invert, mask_size, as_array):
    """Test distance field creation function for expected errors."""
    with pytest.raises(alpha_error[1]):
        d = distance(
            layer=layer,
            alpha=alpha_error[0],
            thresholds=thresholds,
            invert=invert,
            mask_size=mask_size,
            as_array=as_array,
        )


def test_threshold_errors(layer, alpha, thresholds_error, invert, mask_size, as_array):
    """Test distance field creation function for expected errors."""
    with pytest.raises(thresholds_error[1]):
        d = distance(
            layer=layer,
            alpha=alpha,
            thresholds=thresholds_error[0],
            invert=invert,
            mask_size=mask_size,
            as_array=as_array,
        )


def test_invert_errors(layer, alpha, thresholds, invert_error, mask_size, as_array):
    """Test distance field creation function for expected errors."""
    with pytest.raises(invert_error[1]):
        d = distance(
            layer=layer,
            alpha=alpha,
            thresholds=thresholds,
            invert=invert_error[0],
            mask_size=mask_size,
            as_array=as_array,
        )


def test_mask_size_errors(layer, alpha, thresholds, invert, mask_size_error, as_array):
    """Test distance field creation function for expected errors."""
    with pytest.raises(mask_size_error[1]):
        d = distance(
            layer=layer,
            alpha=alpha,
            thresholds=thresholds,
            invert=invert,
            mask_size=mask_size_error[0],
            as_array=as_array,
        )


def test_as_array_errors(layer, alpha, thresholds, invert, mask_size, as_array_error):
    """Test distance field creation function for expected errors."""
    with pytest.raises(as_array_error[1]):
        d = distance(
            layer=layer,
            alpha=alpha,
            thresholds=thresholds,
            invert=invert,
            mask_size=mask_size,
            as_array=as_array_error[0],
        )
