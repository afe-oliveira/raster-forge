from typing import Union

import numpy as np
from rforge.containers.layer import Layer


def check_layer(layer: Union[Layer, np.ndarray]):
    """Checks if a given input, which can be either a Layer object or a Numpy array, is numerical and non-empty. Returns the input array if it meets these criteria."""
    if isinstance(layer, Layer) and layer.array is not None:
        return layer.array
    elif isinstance(layer, np.ndarray) and layer is not None:
        return layer
    else:
        raise TypeError(
            "Layer must be a non-empty Layer object or a non-empty numerical Numpy array."
        )
