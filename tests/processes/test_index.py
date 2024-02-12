import numpy as np
import pytest
from rforge.containers.layer import Layer
from rforge.processes.index import index as compute_index


def test(data_index):
    """Test multispectral index map creation function."""
    index = data_index.get("index", None)
    parameters = data_index.get("parameters", None)
    alpha = data_index.get("alpha", None)
    thresholds = data_index.get("thresholds", None)
    binarize = data_index.get("binarize", None)
    as_array = data_index.get("as_array", None)
    result = data_index.get("result", None)

    i = compute_index(
        index=index,
        parameters=parameters,
        alpha=alpha,
        thresholds=thresholds,
        binarize=binarize,
        as_array=as_array,
    )
    i_array = i.array if as_array else i
    i_count = i_array.shape[-1] if len(i_array.shape) > 2 else 1

    assert (as_array and isinstance(i, np.ndarray)) or (
        not as_array and isinstance(i, Layer)
    )
    assert (alpha is None and i_count == 1) or (alpha is not None and i_count == 2)
    assert i_array == result
    assert alpha is None or (alpha is not None and i_array[-1] == alpha)


def test_errors(data_index_error):
    """Test multispectral index map creation function for expected errors."""
    index = data_index_error.get("index", None)
    parameters = data_index_error.get("parameters", None)
    alpha = data_index_error.get("alpha", None)
    thresholds = data_index_error.get("thresholds", None)
    binarize = data_index_error.get("binarize", None)
    as_array = data_index_error.get("as_array", None)
    error = data_index_error.get("error", None)

    with pytest.raises(error):
        i = compute_index(
            index=index,
            parameters=parameters,
            alpha=alpha,
            thresholds=thresholds,
            binarize=binarize,
            as_array=as_array,
        )
