import hashlib
import pickle

import numpy as np
import pytest

from rforge.library.processes.composite import composite

from tests.files.benchmarks.test_data import COMPOSITE_TEST_DATA

np.random.seed(42)

COMPOSITE_TEST_DATA.clear()

with open("tests/files/benchmarks/composite.pkl", "rb") as file:
    TESTS = pickle.load(file)


def test(layer_list, alpha, gamma, as_array):
    """Test composite creation function."""
    gamma = tuple([0.5 + i * 0.25 for i in range(len(layer_list))]) if gamma else None
    input_code = hashlib.sha256(
        pickle.dumps([layer_list, alpha, gamma, as_array])
    ).hexdigest()
    result = TESTS.get(input_code, None)

    c = composite(layers=layer_list, alpha=alpha, gamma=gamma, as_array=as_array)

    COMPOSITE_TEST_DATA.add(input_code, c)

    assert (as_array and np.allclose(c, result, atol=0.01)) or (
        not as_array and c == result
    )


def test_layers_list_error(layer_list_error, alpha, gamma, as_array):
    """Test composite creation function for expected errors."""
    gamma = (
        tuple([0.5 + i * 0.25 for i in range(len(layer_list_error))]) if gamma else None
    )
    with pytest.raises(layer_list_error[1]):
        c = composite(
            layers=layer_list_error[0], alpha=alpha, gamma=gamma, as_array=as_array
        )


def test_alpha_error(layer_list, alpha_error, gamma, as_array):
    """Test composite creation function for expected errors."""
    gamma = tuple([0.5 + i * 0.25 for i in range(len(layer_list))]) if gamma else None
    with pytest.raises(alpha_error[1]):
        c = composite(
            layers=layer_list, alpha=alpha_error[0], gamma=gamma, as_array=as_array
        )


def test_gamma_type_error(layer_list, alpha, as_array):
    """Test composite creation function for expected errors."""
    gamma = tuple([str(0.5 + i * 0.25) for i in range(len(layer_list))])
    with pytest.raises(TypeError):
        c = composite(layers=layer_list, alpha=alpha, gamma=gamma, as_array=as_array)


def test_gamma_size_error(layer_list, alpha, as_array):
    """Test composite creation function for expected errors."""
    gamma = tuple([0.5 + i * 0.25 for i in range(len(layer_list) + 1)])
    with pytest.raises(TypeError):
        c = composite(layers=layer_list, alpha=alpha, gamma=gamma, as_array=as_array)


def test_as_array_error(layer_list, alpha, gamma, as_array_error):
    """Test composite creation function for expected errors."""
    gamma = tuple([0.5 + i * 0.25 for i in range(len(layer_list))]) if gamma else None
    with pytest.raises(as_array_error[1]):
        c = composite(
            layers=layer_list, alpha=alpha, gamma=gamma, as_array=as_array_error[0]
        )
