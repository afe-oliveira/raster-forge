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
) -> Union[np.ndarray, Layer]:
    """Calculate the distance field of a geographical region.

    Args:
      layer:
        Binary layer data.
      alpha:
        Alpha layer. Defaults to None.
      thresholds:
        Thresholds to use for image binarization. Defaults to None.
      invert:
        If True, inverts the binary layer data before processing. Defaults to False.
      mask_size:
        Size of the mask for distance calculation. Defaults to 3.
      as_array:
        If True, returns the distance field as a Numpy array. Defaults to False.

    Returns:
      Distance field layer.
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
