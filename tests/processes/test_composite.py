import numpy as np
import pytest
from rforge.containers.layer import Layer
from rforge.processes.composite import composite


def test(data_composite):
    """Test composite creation function."""
    layers = data_composite.get("layers", None)
    alpha = data_composite.get("alpha", None)
    gamma = data_composite.get("gamma", None)
    as_array = data_composite.get("as_array", None)

    c = composite(layers=layers, alpha=alpha, gamma=gamma, as_array=as_array)
    c_result = c if as_array else c.array

    for i in range(len(layers)):
        layers[i] = layers[i].array if isinstance(layers[i], Layer) else layers[i]

    alpha = alpha.array if isinstance(alpha, Layer) else alpha

    assert (alpha is None and np.array_equal(c_result, np.dstack(layers))) or (
        alpha is not None and np.array_equal(c_result, np.dstack([layers, alpha]))
    )


def test_errors(data_composite_error):
    """Test composite creation function for expected errors."""
    layers = data_composite_error.get("layers", None)
    alpha = data_composite_error.get("alpha", None)
    gamma = data_composite_error.get("gamma", None)
    as_array = data_composite_error.get("as_array", None)
    error = data_composite_error.get("error", None)

    with pytest.raises(error):
        c = composite(layers=layers, alpha=alpha, gamma=gamma, as_array=as_array)
