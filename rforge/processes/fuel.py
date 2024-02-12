import math
from typing import Optional, Union

import numpy as np
from rforge.containers.layer import Layer
from rforge.tools.data_validation import check_layer


def fuel(
    coverage: Union[Layer, np.ndarray],
    height: Union[Layer, np.ndarray],
    distance: Union[Layer, np.ndarray],
    water: Union[Layer, np.ndarray],
    artificial: Union[Layer, np.ndarray],
    models: tuple[int, int, int],
    tree_height: float,
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    as_array: bool = False,
):
    """Calculate the fuel of the terrain based on a fuel models.

    Args:
      layer:
        Layer data of the terrain.

    Returns:
      Fuel raster map.
    """
    coverage = check_layer(coverage)
    height = check_layer(height)
    distance = check_layer(distance)
    water = check_layer(water)
    artificial = check_layer(artificial)

    # Estimate Sub Layer Average
    sub_coverage_average = np.mean(np.where(height < tree_height, coverage, 0))

    # Start With a Full Map
    result = np.full(coverage.shape, models[2])

    # Assign Leafy Vegetation Value (Trees)
    if sub_coverage_average > (100 / 3):
        result = np.where(height >= tree_height, models[1], result)  # Trees + Shrubbery
    else:
        result = np.where(height >= tree_height, models[0], result)  # Trees

    # Assign Bare Soil
    result = np.where(distance >= math.floor(distance.max()), 99, result)
    result = np.where(
        np.logical_and(
            distance >= (math.floor(distance.max() * 0.95)),
            distance < (math.floor(distance.max())),
        ),
        224,
        result,
    )

    # Assign Artificial Structures
    result = np.where(np.logical_and(artificial > 0, result == 99), 91, result)

    # Assign Water
    result = np.where(water > 0, 98, result)

    if alpha is not None:
        alpha = check_layer(alpha)
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
