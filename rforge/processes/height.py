from typing import Any, Optional, Union

import numpy as np
from numpy import dtype, generic, ndarray
from rforge.containers.layer import Layer
from rforge.tools.data_validation import check_layer
from rforge.tools.exceptions import Errors


def height(
    dtm: Union[Layer, np.ndarray],
    dsm: Union[Layer, np.ndarray],
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    as_array: bool = False,
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
    dtm = check_layer(dtm)
    dsm = check_layer(dsm)

    result = dsm - dtm

    if alpha is not None:
        alpha = check_layer(alpha)
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
