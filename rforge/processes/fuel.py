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
    is_array = True
    result = coverage.array

    if is_array:
        return result
    else:
        return Layer(result)
