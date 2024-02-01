from typing import Optional, Union

import numpy as np

from rforge.containers.layer import Layer
from rforge.tools.exceptions import ErrorMessages


def slope(
    dem: Union[Layer, np.ndarray],
    units: str = "degrees",
    alpha: Optional[np.ndarray] = None,
) -> Layer | np.ndarray:
    """Calculate the slope of a terrain based on a Digital Elevation Model (DEM).

    Args:
      dem:
        Digital elevation model data representing the terrain.
      units:
        Units for computing the slope.

    Returns:
      Slope raster map in the desired unit.
    """
    is_array = False
    if isinstance(dem, Layer) and dem.array is not None:
        array = dem.array
    elif (
        isinstance(dem, np.ndarray)
        and dem is not None
        and np.issubdtype(dem.dtype, np.number)
    ):
        array = dem
        is_array = True
    else:
        raise TypeError(
            ErrorMessages.bad_input(
                name="dem", expected_type="a numerical Layer or array"
            )
        )

    result = np.arctan(
        np.sqrt(
            np.power(np.gradient(array, axis=(0, 1))[0], 2)
            + np.power(np.gradient(array, axis=(0, 1))[1], 2)
        )
    )

    if units in ["degrees", "radians"]:
        if units == "degrees":
            result = np.degrees(result)
    else:
        raise TypeError(
            ErrorMessages.bad_input(
                name="units", expected_type="'degrees' or 'radians'"
            )
        )

    if alpha is not None:
        result = np.dstack([result, alpha])

    if is_array:
        return result
    else:
        return Layer(result)


def aspect(
    dem: Union[Layer, np.ndarray],
    units: str = "degrees",
    alpha: Optional[np.ndarray] = None,
) -> Layer | np.ndarray:
    """Calculate the aspect of a terrain slope based on a Digital Elevation Model (DEM).

    Args:
      dem:
        Digital elevation model data representing the terrain.
      units:
        Units for computing the aspect.

    Returns:
      Aspect raster map.
    """
    is_array = False
    if isinstance(dem, Layer) and dem.array is not None:
        array = dem.array
    elif (
        isinstance(dem, np.ndarray)
        and dem is not None
        and np.issubdtype(dem.dtype, np.number)
    ):
        array = dem
        is_array = True
    else:
        raise TypeError(
            ErrorMessages.bad_input(
                name="dem", expected_type="a numerical Layer or array"
            )
        )

    result = np.arctan2(-np.gradient(array, axis=0), np.gradient(array, axis=1))

    if units in ["degrees", "radians"]:
        if units == "degrees":
            result = np.degrees(result)
    else:
        raise TypeError(
            ErrorMessages.bad_input(
                name="units", expected_type="'degrees' or 'radians'"
            )
        )

    if alpha is not None:
        result = np.dstack([result, alpha])

    if is_array:
        return result
    else:
        return Layer(result)
