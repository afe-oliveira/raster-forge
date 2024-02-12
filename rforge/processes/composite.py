from typing import Any, Optional, Union

import numpy as np
from numpy import dtype, generic, ndarray
from rforge.containers.layer import Layer
from rforge.tools.data_validation import check_layer
from rforge.tools.exceptions import Errors

PRESET_COMPOSITES = {
    "True Color": ["Red", "Green", "Blue"],
    "CIR": ["NIR", "Red", "Green"],
}


def composite(
    layers: Union[list[Layer], list[np.ndarray]],
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    gamma: Optional[list[float]] = None,
    as_array: bool = False,
) -> ndarray[Any, dtype[generic | generic | Any]] | ndarray[Any, dtype[Any]] | Layer:
    """Stacks all provided layers into a single array in order, including alpha. Applies gamma correction if provided.

    Args:
      layers:
        List of raster layers.
      alpha:
        Alpha layer.
      gamma:
        List of gamma values.
      array:
        Indicates if result should be returned as a Numpy array instead of a Layer object.
    Returns:
      Stacked composite layer.
    """
    arrays = [check_layer(layer) for layer in layers]
    result = np.dstack(arrays)

    if gamma is not None and isinstance(gamma, list) and len(arrays) == len(gamma):
        if all(isinstance(element, (int, float)) for element in gamma):
            gamma = [float(element) for element in gamma]
            result = np.power(result, np.array(gamma)[:, np.newaxis, np.newaxis])
        else:
            raise TypeError(
                Errors.bad_input(name="gamma", expected_type="a list of numeric values")
            )

    if alpha is not None:
        alpha = check_layer(alpha)
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
