from typing import Optional, Union

import cv2
import numpy as np
from rforge.containers.layer import Layer
from rforge.tools.data_validation import check_layer


def distance(
    layer: Union[Layer, np.ndarray],
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    thresholds: Optional[tuple[float, float]] = None,
    invert: bool = False,
    mask_size: int = 3,
    as_array: bool = False,
):
    """Calculate the distance of terrain features.

    Args:
      layer:
        Binary layer data.

    Returns:
      Distance raster map.
    """
    array = check_layer(layer)

    if thresholds is not None:
        mask = np.logical_and(array >= thresholds[0], array <= thresholds[1])
        if invert:
            array = np.where(mask, 0, 255)
        else:
            array = np.where(mask, 255, 0)

    result = cv2.distanceTransform(np.uint8(array), cv2.DIST_L2, mask_size)
    result = abs(result.max() - result)

    if alpha is not None:
        alpha = check_layer(alpha)
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
