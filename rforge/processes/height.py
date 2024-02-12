from typing import Optional, Union

import numpy as np
from rforge.containers.layer import Layer
from rforge.tools.data_validation import check_layer


def height(
    dtm: Union[Layer, np.ndarray],
    dsm: Union[Layer, np.ndarray],
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    as_array: bool = False,
) -> np.ndarray | Layer:
    """Calculate the height difference between the Digital Terrain Model (DTM) and the Digital Surface Model (DSM).

    Args:
      dtm:
        Digital Terrain Model (DTM) layer data.
      dsm:
        Digital Surface Model (DSM) layer data.
      alpha:
        Alpha layer. Defaults to None.
      as_array:
        If True, returns the distance field as a Numpy array. Defaults to False.

    Returns:
      Height difference raster map.
    """
    dtm = check_layer(dtm)
    dsm = check_layer(dsm)

    result = dsm - dtm

    if alpha is not None:
        alpha = check_layer(alpha)
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
