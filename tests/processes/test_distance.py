import numpy as np
import pytest
from rforge.processes.distance import distance


def test(data_distance):
    """Test distance field creation function."""
    layer = data_distance.get("layer", None)
    alpha = data_distance.get("alpha", None)
    thresholds = data_distance.get("thresholds", None)
    invert = data_distance.get("invert", None)
    mask_size = data_distance.get("mask_size", None)
    as_array = data_distance.get("as_array", None)
    result = data_distance.get("result", None)

    d = distance(
        layer=layer,
        alpha=alpha,
        thresholds=thresholds,
        invert=invert,
        mask_size=mask_size,
        as_array=as_array,
    )
    assert (as_array and np.array_equal(d, result)) or (not as_array and d == result)


def test_errors(data_distance_error):
    """Test distance field creation function for expected errors."""
    layer = data_distance_error.get("layer", None)
    alpha = data_distance_error.get("alpha", None)
    thresholds = data_distance_error.get("thresholds", None)
    invert = data_distance_error.get("invert", None)
    mask_size = data_distance_error.get("mask_size", None)
    as_array = data_distance_error.get("as_array", None)
    error = data_distance_error.get("error", None)

    with pytest.raises(error):
        d = distance(
            layer=layer,
            alpha=alpha,
            thresholds=thresholds,
            invert=invert,
            mask_size=mask_size,
            as_array=as_array,
        )
