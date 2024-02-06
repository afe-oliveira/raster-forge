from typing import Optional, Union

import numpy as np
from scipy.ndimage import distance_transform_edt

from rforge.containers.layer import Layer
from rforge.tools.exceptions import ErrorMessages


def distance(
    layer: Union[Layer, np.ndarray],
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    thresholds: Optional[tuple[float, float]] = None,
    invert: bool = False
):
    """Calculate the distance of terrain features.

    Args:
      layer:
        Binary layer data.

    Returns:
      Distance raster map.
    """
    is_array = False
    if isinstance(layer, Layer) and layer.array is not None:
        array = layer.array
    elif (
        isinstance(layer, np.ndarray)
        and layer is not None
        and np.issubdtype(layer.dtype, np.number)
    ):
        array = layer
        is_array = True
    else:
        raise TypeError(
            ErrorMessages.bad_input(
                name="layer", expected_type="a numerical Layer or array"
            )
        )

    if thresholds is not None:
        mask = np.logical_and(array >= thresholds[0], array <= thresholds[1])
        if invert:
            array = np.uint8(np.where(mask, 0, 255))
        else:
            array = np.uint8(np.where(mask, 255, 0))

    result = distance_transform_edt(array)
    result = abs(result.max() - result)

    if alpha is not None:
        if isinstance(alpha, Layer) and alpha.array is not None:
            result[alpha.array == 0] = result.max()
        elif (
            isinstance(alpha, np.ndarray)
            and alpha is not None
            and np.issubdtype(alpha.dtype, np.number)
        ):
            result[alpha == 0] = result.max()
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
