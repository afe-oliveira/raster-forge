import hashlib
import pickle

import numpy as np
import pytest
from rforge.processes.height import height

from tests.files.benchmarks.test_data import HEIGHT_TEST_DATA

np.random.seed(42)

HEIGHT_TEST_DATA.clear()

with open("tests/files/benchmarks/height.pkl", "rb") as file:
    TESTS = pickle.load(file)


def test(dtm, dsm, alpha, as_array):
    """Test height map creation function."""
    input_code = hashlib.sha256(pickle.dumps([dtm, dsm, alpha, as_array])).hexdigest()
    result = TESTS.get(input_code, None)

    h = height(dtm=dtm, dsm=dsm, alpha=alpha, as_array=as_array)

    HEIGHT_TEST_DATA.add(input_code, h)

    assert (as_array and np.allclose(h, result, atol=0.01)) or (
        not as_array and h == result
    )


def test_dtm_error(layer_error, dsm, alpha, as_array):
    """Test height map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        h = height(dtm=layer_error[0], dsm=dsm, alpha=alpha, as_array=as_array)


def test_dsm_error(dtm, layer_error, alpha, as_array):
    """Test height map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        h = height(dtm=dtm, dsm=layer_error[0], alpha=alpha, as_array=as_array)


def test_alpha_error(dtm, dsm, alpha_error, as_array):
    """Test height map creation function for expected errors."""
    with pytest.raises(alpha_error[1]):
        h = height(dtm=dtm, dsm=dsm, alpha=alpha_error[0], as_array=as_array)


def test_as_array_error(dtm, dsm, alpha, as_array_error):
    """Test height map creation function for expected errors."""
    with pytest.raises(as_array_error[1]):
        h = height(dtm=dtm, dsm=dsm, alpha=alpha, as_array=as_array_error[0])
