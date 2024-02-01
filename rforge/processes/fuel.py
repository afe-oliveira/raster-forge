from typing import Optional, Union

import numpy as np

from rforge.containers.layer import Layer
from rforge.tools.exceptions import ErrorMessages


def fuel(
    coverage,
    height,
    bareness,
    water,
    artificial,
    cir,
    alpha: Optional[Union[Layer, np.ndarray]] = None,
):
    """Calculate the fuel of the terrain based on a fuel models.

    Args:
      layer:
        Layer data of the terrain.

    Returns:
      Fuel raster map.
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

    result = array

    if is_array:
        return result
    else:
        return Layer(result)
