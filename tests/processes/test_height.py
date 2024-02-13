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
    assert (as_array and np.array_equal(h, result)) or (not as_array and h == result)

def test_errors(data_height_error):
    """Test height map creation function for expected errors."""
    dtm = data_height_error.get("dtm", None)
    dsm = data_height_error.get("dsm", None)
    alpha = data_height_error.get("alpha", None)
    as_array = data_height_error.get("as_array", None)
    error = data_height_error.get("error", None)

    with pytest.raises(error):
        h = height(dtm=dtm, dsm=dsm, alpha=alpha, as_array=as_array)
