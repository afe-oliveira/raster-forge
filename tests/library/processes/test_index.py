import hashlib
import pickle

import numpy as np
import pytest
from rforge.library.processes.index import index

from tests.files.benchmarks.test_data import INDEX_TEST_DATA

np.random.seed(42)

INDEX_TEST_DATA.clear()

with open("tests/files/benchmarks/index.pkl", "rb") as file:
    TESTS = pickle.load(file)


def test(index_id, index_parameters, alpha, thresholds, binarize, as_array):
    """Test multispectral index map creation function."""
    input_code = hashlib.sha256(
        pickle.dumps(
            [index_id, index_parameters, alpha, thresholds, binarize, as_array]
        )
    ).hexdigest()
    result = TESTS.get(input_code, None)

    i = index(
        index_id=index_id,
        parameters=index_parameters,
        alpha=alpha,
        thresholds=thresholds,
        binarize=binarize,
        as_array=as_array,
    )

    INDEX_TEST_DATA.add(input_code, i)

    assert (as_array and np.allclose(i, result, atol=0.01)) or (
        not as_array and i == result
    )


def test_index_id_error(
    index_id_error, index_parameters, alpha, thresholds, binarize, as_array
):
    """Test multispectral index map creation function for expected errors."""
    with pytest.raises(index_id_error[1]):
        i = index(
            index_id=index_id_error[0],
            parameters=index_parameters,
            alpha=alpha,
            thresholds=thresholds,
            binarize=binarize,
            as_array=as_array,
        )


def test_index_parameters_error(
    index_id, index_parameters_error, alpha, thresholds, binarize, as_array
):
    """Test multispectral index map creation function for expected errors."""
    with pytest.raises(index_parameters_error[1]):
        i = index(
            index_id=index_id,
            parameters=index_parameters_error[0],
            alpha=alpha,
            thresholds=thresholds,
            binarize=binarize,
            as_array=as_array,
        )


def test_alpha_error(
    index_id, index_parameters, alpha_error, thresholds, binarize, as_array
):
    """Test multispectral index map creation function for expected errors."""
    with pytest.raises(alpha_error[1]):
        i = index(
            index_id=index_id,
            parameters=index_parameters,
            alpha=alpha_error[0],
            thresholds=thresholds,
            binarize=binarize,
            as_array=as_array,
        )


def test_treshold_error(
    index_id, index_parameters, alpha, thresholds_error, binarize, as_array
):
    """Test multispectral index map creation function for expected errors."""
    with pytest.raises(thresholds_error[1]):
        i = index(
            index_id=index_id,
            parameters=index_parameters,
            alpha=alpha,
            thresholds=thresholds_error[0],
            binarize=binarize,
            as_array=as_array,
        )


def test_binarize_error(
    index_id, index_parameters, alpha, thresholds, binarize_error, as_array
):
    """Test multispectral index map creation function for expected errors."""
    with pytest.raises(binarize_error[1]):
        i = index(
            index_id=index_id,
            parameters=index_parameters,
            alpha=alpha,
            thresholds=thresholds,
            binarize=binarize_error[0],
            as_array=as_array,
        )


def test_as_array_error(
    index_id, index_parameters, alpha, thresholds, binarize, as_array_error
):
    """Test multispectral index map creation function for expected errors."""
    with pytest.raises(as_array_error[1]):
        i = index(
            index_id=index_id,
            parameters=index_parameters,
            alpha=alpha,
            thresholds=thresholds,
            binarize=binarize,
            as_array=as_array_error[0],
        )
