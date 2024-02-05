from typing import Any, Optional, Union

import numpy as np
from numpy import dtype, generic, ndarray
from rforge.containers.layer import Layer
from rforge.tools.exceptions import ErrorMessages

PRESET_COMPOSITES = {
    "True Color": ["Red", "Green", "Blue"],
    "CIR": ["NIR", "Red", "Green"],
}


def composite(
    layers: Union[list[Layer], list[np.ndarray]],
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    gamma: Optional[list[float]] = None,
) -> ndarray[Any, dtype[generic | generic | Any]] | ndarray[Any, dtype[Any]] | Layer:
    """Stacks all provided layers into a single array in order. Applies gamma correction.

    Args:
      layers:
        List of raster layers.
      alpha:
        Alpha layer.
      gamma:
        List of gamma values.
    Returns:
      Stacked composite layer.
    """
    is_array = False
    if all((isinstance(layer, Layer) and layer.array is not None) for layer in layers):
        arrays = [layer.array for layer in layers]
    elif all(
        (
            isinstance(layer, np.ndarray)
            and layer is not None
            and np.issubdtype(layer.dtype, np.number)
        )
        for layer in layers
    ):
        arrays = [layer for layer in layers]
        is_array = True
    else:
        raise TypeError(
            ErrorMessages.bad_input(
                name="layers", expected_type="a list of numerical Layers or arrays"
            )
        )

    result = np.dstack(arrays)

    if gamma is not None and isinstance(gamma, list) and len(arrays) == len(gamma):
        if all(isinstance(element, (int, float)) for element in gamma):
            gamma = [float(element) for element in gamma]

            aux = np.zeros_like(result)
            for i in range(len(gamma)):
                aux[:, :, i] = np.power(result[:, :, i], gamma[i])
            result = aux
        else:
            raise TypeError(
                ErrorMessages.bad_input(
                    name="gamma", expected_type="a tuple of numeric values"
                )
            )

    if alpha is not None:
        if isinstance(alpha, Layer) and alpha.array is not None:
            result = np.dstack([result, alpha.array])
        elif (
            isinstance(alpha, np.ndarray)
            and alpha is not None
            and np.issubdtype(alpha.dtype, np.number)
        ):
            result = np.dstack([result, alpha])
        else:
            raise TypeError(
                ErrorMessages.bad_input(
                    name="gamma", expected_type="a numerical Layer or array"
                )
            )

    if is_array:
        return result
    else:
        return Layer(result)
