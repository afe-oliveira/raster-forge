import hashlib
import pickle
import random

import numpy as np
from rforge.processes.composite import composite

from tests.files.benchmarks.test_data import (
    COMPOSITE_TEST_DATA,
    COMPOSITE_TEST_ERROR_DATA,
)

np.random.seed(42)

COMPOSITE_TEST_DATA.clear()
COMPOSITE_TEST_ERROR_DATA.clear()

with open("tests/files/benchmarks/composite.pkl", "rb") as file:
    TESTS = pickle.load(file)


def test(data_layer_list, data_alpha, data_gamma, data_as_array):
    """Test composite creation function."""
    gamma = (
        tuple([(random.uniform(0, 2)) for _ in data_layer_list]) if data_gamma else None
    )
    print(gamma)
    input_code = hashlib.sha256(
        pickle.dumps([data_layer_list, data_gamma, data_alpha, data_as_array])
    ).hexdigest()
    result = TESTS[input_code]

    c = composite(
        layers=data_layer_list, alpha=data_alpha, gamma=gamma, as_array=data_as_array
    )

    COMPOSITE_TEST_DATA.add(input_code, c)

    assert (data_as_array and np.allclose(c, result, atol=0.01)) or (
        not data_as_array and c == result
    )


"""
def test_errors(data_composite_error):
    \"\"\"Test composite creation function for expected errors.\"\"\"
    layers = data_composite_error.get("layers", None)
    alpha = data_composite_error.get("alpha", None)
    gamma = data_composite_error.get("gamma", None)
    as_array = data_composite_error.get("as_array", None)
    error = data_composite_error.get("error", None)

    with pytest.raises(error):
        c = composite(layers=layers, alpha=alpha, gamma=gamma, as_array=as_array)
"""
