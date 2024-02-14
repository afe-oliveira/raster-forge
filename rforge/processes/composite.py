from typing import Optional, Union

import numpy as np
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
    gamma: Optional[Union[list, tuple]] = None,
    as_array: bool = False,
) -> Union[np.ndarray, Layer]:
    """Stacks all provided layers into a single array in order, including alpha. Applies gamma correction if provided.

    Args:
      layers:
        List of raster layers.
      alpha:
        Alpha layer. Defaults to None.
      gamma:
        List of gamma values to apply to each layer. Defaults to None.
      as_array:
        If True, returns the distance field as a Numpy array. Defaults to False.

    Returns:
      Stacked composite layer.

    Raises:
      TypeError:
        If inputs are not of the accepted type.
    """
    if not isinstance(as_array, bool):
        raise TypeError(Errors.bad_input(name="as_array", expected_type="a boolean"))
    arrays = [check_layer(layer) for layer in layers]
    result = np.dstack(arrays)

    if gamma is not None:
        if isinstance(gamma, (list, tuple)) and len(arrays) == len(gamma):
            if all(isinstance(element, (int, float)) for element in gamma):
                gamma = list(map(float, gamma))
                result = np.power(result, np.array(gamma))
            else:
                raise TypeError(
                    Errors.bad_input(
                        name="gamma", expected_type="a list or tuple of numeric values"
                    )
                )
        else:
            raise TypeError(
                Errors.bad_input(
                    name="gamma",
                    expected_type="the same amount of elements as there are layers",
                )
            )

    if alpha is not None:
        alpha = check_layer(alpha)
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
