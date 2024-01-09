from typing import Optional, Union

import cv2
import numpy as np

from RasterForge.containers.layer import Layer
from RasterForge.tools.exceptions import ErrorMessages


def distance(
    layer: Union[Layer, np.ndarray], alpha: Optional[Union[Layer, np.ndarray]] = None
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

    result = cv2.distanceTransform(array, cv2.DIST_L2, 5)
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
