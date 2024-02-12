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
    c_count = c.array.shape[-1] if len(c.array.shape) > 2 else 1
    if as_array:
        c_result = c[:, :, :-1] if c_count > 2 else c
    else:
        c_result = c.array[:, :, :-1] if c_count > 2 else c.array
    c_alpha = c.array[:, :, -1] if alpha is not None else None

    assert (as_array and isinstance(c, np.ndarray)) or (
        not as_array and isinstance(c, Layer)
    )
    assert (alpha is None and c_count == len(layers)) or (
        alpha is not None and c_count == len(layers) + 1
    )
    assert c_result == layers
    assert c_alpha == alpha


def test_errors(data_composite_error):
    """Test composite creation function for expected errors."""
    layers = data_composite_error.get("layers", None)
    alpha = data_composite_error.get("alpha", None)
    gamma = data_composite_error.get("gamma", None)
    as_array = data_composite_error.get("as_array", None)
    error = data_composite_error.get("error", None)

    with pytest.raises(error):
        c = composite(layers=layers, alpha=alpha, gamma=gamma, as_array=as_array)
