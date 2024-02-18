from typing import Union

import numpy as np
from rforge.containers.layer import Layer


def check_layer(layer: Union[Layer, np.ndarray]):
    """
    Check if a given input, which can be either a Layer object or a NumPy array, is numerical and non-empty.

    Args:
      layer:
        Input data, which can be a Layer object or a NumPy array.

    Returns:
      The input array if it meets the criteria.

    Raises:
      TypeError:
        If the input is not a non-empty Layer object or a non-empty numerical NumPy array.
    """
    if (
        isinstance(layer, Layer)
        and layer.array is not None
        and np.isreal(layer.array).all()
    ):
        return layer.array
    elif isinstance(layer, np.ndarray) and layer is not None and np.isreal(layer).all():
        return layer
    else:
        raise TypeError(
            "Layer must be a non-empty Layer object or a non-empty numerical Numpy array."
        )
