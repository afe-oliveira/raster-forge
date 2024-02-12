import numpy as np
import pytest
from rforge.containers.layer import Layer
from rforge.processes.height import height


def test(data_height):
    """Test height map creation function."""
    dtm = data_height.get("dtm", None)
    dsm = data_height.get("dsm", None)
    alpha = data_height.get("alpha", None)
    as_array = data_height.get("as_array", None)
    result = data_height.get("result", None)

    h = height(dtm=dtm, dsm=dsm, alpha=alpha, as_array=as_array)
    h_array = h.array if as_array else h
    h_count = h_array.shape[-1] if len(h_array.shape) > 2 else 1

    assert (as_array and isinstance(h, np.ndarray)) or (
        not as_array and isinstance(h, Layer)
    )
    assert (alpha is None and h_count == 1) or (alpha is not None and h_count == 2)
    assert h_array == result
    assert alpha is None or (alpha is not None and h_array[-1] == alpha)


def test_errors(data_height_error):
    """Test height map creation function for expected errors."""
    dtm = data_height_error.get("dtm", None)
    dsm = data_height_error.get("dsm", None)
    alpha = data_height_error.get("alpha", None)
    as_array = data_height_error.get("as_array", None)
    error = data_height_error.get("error", None)

    with pytest.raises(error):
        h = height(dtm=dtm, dsm=dsm, alpha=alpha, as_array=as_array)