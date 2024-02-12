import numpy as np
import pytest
from rforge.containers.layer import Layer
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
    d_array = d.array if as_array else d
    d_count = d_array.shape[-1] if len(d_array.shape) > 2 else 1

    assert (as_array and isinstance(d, np.ndarray)) or (
        not as_array and isinstance(d, Layer)
    )
    assert (alpha is None and d_count == 1) or (alpha is not None and d_count == 2)
    assert (d_count == 1 and d_array == result) or (
        d_count == 2 and d_array[:, :, 0] == result
    )
    assert alpha is None or (alpha is not None and d_array[:, :, -1] == alpha)


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
