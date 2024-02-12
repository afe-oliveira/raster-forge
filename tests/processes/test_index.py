import numpy as np
import pytest
from rforge.containers.layer import Layer
from rforge.processes.index import index


def test(data_index):
    """Test multispectral index map creation function."""
    index_id = data_index.get("index", None)
    parameters = data_index.get("parameters", None)
    alpha = data_index.get("alpha", None)
    thresholds = data_index.get("thresholds", None)
    binarize = data_index.get("binarize", None)
    as_array = data_index.get("as_array", None)
    result = data_index.get("result", None)

    i = index(
        index_id=index_id,
        parameters=parameters,
        alpha=alpha,
        thresholds=thresholds,
        binarize=binarize,
        as_array=as_array,
    )
    i_count = i.array.shape[-1] if len(i.array.shape) > 2 else 1
    if as_array:
        i_result = i[:, :, :-1] if i_count > 2 else i
    else:
        i_result = i.array[:, :, :-1] if i_count > 2 else i.array
    i_alpha = i.array[:, :, -1] if alpha is not None else None

    assert (as_array and isinstance(i, np.ndarray)) or (
            not as_array and isinstance(i, Layer)
    )
    assert (alpha is None and i_count == 1) or (
            alpha is not None and i_count == 2
    )
    assert i_result == result
    assert i_alpha == alpha


def test_errors(data_index_error):
    """Test multispectral index map creation function for expected errors."""
    index_id = data_index_error.get("index", None)
    parameters = data_index_error.get("parameters", None)
    alpha = data_index_error.get("alpha", None)
    thresholds = data_index_error.get("thresholds", None)
    binarize = data_index_error.get("binarize", None)
    as_array = data_index_error.get("as_array", None)
    error = data_index_error.get("error", None)

    with pytest.raises(error):
        i = index(
            index_id=index_id,
            parameters=parameters,
            alpha=alpha,
            thresholds=thresholds,
            binarize=binarize,
            as_array=as_array,
        )
