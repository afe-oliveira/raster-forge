import numpy as np
import pytest
from rforge.processes.composite import composite


def test(data_composite):
    """Test composite creation function."""
    layers = data_composite.get("layers", None)
    alpha = data_composite.get("alpha", None)
    gamma = data_composite.get("gamma", None)
    as_array = data_composite.get("as_array", None)
    result = data_composite.get("result", None)

    c = composite(layers=layers, alpha=alpha, gamma=gamma, as_array=as_array)
    if as_array:
        np.testing.assert_array_equal(c, result, verbose=True)
    else:
        assert c == result


def test_errors(data_composite_error):
    """Test composite creation function for expected errors."""
    layers = data_composite_error.get("layers", None)
    alpha = data_composite_error.get("alpha", None)
    gamma = data_composite_error.get("gamma", None)
    as_array = data_composite_error.get("as_array", None)
    error = data_composite_error.get("error", None)

    with pytest.raises(error):
        c = composite(layers=layers, alpha=alpha, gamma=gamma, as_array=as_array)
