import math
from typing import Optional, Union

import numpy as np
from rforge.containers.layer import Layer
from rforge.tools.exceptions import ErrorMessages


def fuel(
    coverage: Union[Layer, np.ndarray],
    height: Union[Layer, np.ndarray],
    distance: Union[Layer, np.ndarray],
    water: Union[Layer, np.ndarray],
    artificial: Union[Layer, np.ndarray],
    models: tuple[int, int, int],
    tree_height: float,
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
    if all(
        (isinstance(layer, Layer) and layer.array is not None)
        for layer in [coverage, height, distance, water, artificial]
    ):
        coverage = coverage.array
        height = height.array
        distance = distance.array
        water = water.array
        artificial = artificial.array
    elif all(
        (
            isinstance(layer, np.ndarray)
            and layer is not None
            and np.issubdtype(layer.dtype, np.number)
        )
        for layer in [coverage, height, distance, water, artificial]
    ):
        is_array = True
    else:
        raise TypeError(
            ErrorMessages.bad_input(
                name="layers", expected_type="a list of numerical Layers or arrays"
            )
        )

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
        if isinstance(alpha, Layer) and alpha.array is not None:
            result = np.dstack([result, alpha.array])
        elif (
            isinstance(alpha, np.ndarray)
            and alpha is not None
            and np.issubdtype(alpha.dtype, np.number)
        ):
            result = np.dstack([result, alpha])
        else:
            raise TypeError(
                ErrorMessages.bad_input(
                    name="alpha", expected_type="a numerical Layer or array"
                )
            )

    if is_array:
        return result
    else:
        return Layer(result)
