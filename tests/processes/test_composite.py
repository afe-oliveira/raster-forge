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
    c_array = c.array if as_array else c
    c_count = c_array.shape[-1] if len(c_array.shape) > 2 else 1

    assert (as_array and isinstance(c, np.ndarray)) or (
        not as_array and isinstance(c, Layer)
    )
    assert (alpha is None and c_count == len(layers) + 1) or (
        alpha is not None and c_count == len(layers)
    )
    for i, layer in enumerate(c.array):
        assert layer == layers[:, :, i]
    assert alpha is None or (alpha is not None and c_array[:, :, -1] == alpha)


def test_errors(data_layer_init):
    """Test composite creation function for expected errors."""
    layers = data_layer_init.get("layers", None)
    alpha = data_layer_init.get("alpha", None)
    gamma = data_layer_init.get("gamma", None)
    as_array = data_layer_init.get("as_array", None)
    error = data_layer_init.get("error", None)

    with pytest.raises(error):
        c = composite(layers=layers, alpha=alpha, gamma=gamma, as_array=as_array)
