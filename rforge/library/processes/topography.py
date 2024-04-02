from typing import Optional, Union

import numpy as np
from rforge.library.containers.layer import Layer
from rforge.library.tools.data_validation import check_layer
from rforge.library.tools.exceptions import Errors


def slope(
    dem: Union[Layer, np.ndarray],
    units: str = "degrees",
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    as_array: bool = False,
) -> Union[np.ndarray, Layer]:
    """Calculate the slope of a terrain based on a Digital Elevation Model (DEM).

    Args:
      dem:
        Digital elevation model data representing the terrain.
      units:
        Units for computing the slope. Can be 'degrees' or 'radians'.
      alpha:
        Alpha layer. Defaults to None.
      as_array:
        If True, return the result as a Numpy array. Defaults to False.

    Returns:
      Slope map in the desired unit.

    Raises:
      TypeError:
        If inputs are not of the accepted type.
    """
    array = check_layer(dem)
    if alpha is not None:
        alpha = check_layer(alpha)
    if units not in ["degrees", "radians"]:
        raise TypeError(
            Errors.bad_input(name="units", expected_type="'degrees' or 'radians'")
        )
    if not isinstance(as_array, bool):
        raise TypeError(Errors.bad_input(name="as_array", expected_type="a boolean"))

    result = np.arctan(
        np.sqrt(
            np.power(np.gradient(array, axis=(0, 1))[0], 2)
            + np.power(np.gradient(array, axis=(0, 1))[1], 2)
        )
    )

    if units == "degrees":
        result = np.degrees(result)

    if alpha is not None:
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)


def aspect(
    dem: Union[Layer, np.ndarray],
    units: str = "degrees",
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    as_array: bool = False,
) -> Union[np.ndarray, Layer]:
    """Calculate the aspect of a terrain slope based on a Digital Elevation Model (DEM).

    Args:
      dem:
        Digital elevation model data representing the terrain.
      units:
        Units for computing the slope. Can be 'degrees' or 'radians'.
      alpha:
        Alpha layer. Defaults to None.
      as_array:
        If True, return the result as a Numpy array. Defaults to False.

    Returns:
      Aspect map in the desired unit.
    """
    array = check_layer(dem)
    if alpha is not None:
        alpha = check_layer(alpha)
    if units not in ["degrees", "radians"]:
        raise TypeError(
            Errors.bad_input(name="units", expected_type="'degrees' or 'radians'")
        )
    if not isinstance(as_array, bool):
        raise TypeError(Errors.bad_input(name="as_array", expected_type="a boolean"))

    result = np.arctan2(-np.gradient(array, axis=0), np.gradient(array, axis=1))

    if units == "degrees":
        result = np.degrees(result)

    if alpha is not None:
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
