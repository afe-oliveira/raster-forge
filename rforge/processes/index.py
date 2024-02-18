from typing import Optional, Union

import numpy as np
import spyndex
from rforge.containers.layer import Layer
from rforge.tools.data_validation import check_layer
from rforge.tools.exceptions import Errors


def index(
    index_id: str,
    parameters: dict,
    alpha: Optional[Union[Layer, np.ndarray]] = None,
    thresholds: Optional[Union[list, tuple]] = None,
    binarize: bool = False,
    as_array: bool = False,
) -> Union[np.ndarray, Layer]:
    """
    Compute an index from the input parameters.

    Args:
      index_id:
        Identifier of index to compute
      parameters:
        Dictionary of parameters required for index computation.
      alpha:
        Alpha layer. Defaults to None.
      thresholds:
        Thresholds for binarization or clipping. Defaults to None.
      binarize:
        If True, binarize the result based on the thresholds defined. Defaults to False.
      as_array:
        If True, return the result as a Numpy array. Defaults to False.

    Returns:
      Computed index as a numpy array.

    Raises:
      TypeError:
        If inputs are not of the accepted type.
    """
    # Data Validation
    for key, value in parameters.items():
        aux_value = check_layer(value)
        parameters[key] = aux_value
    if alpha is not None:
        alpha = check_layer(alpha)
    if thresholds is not None:
        if thresholds is not None and not (
            isinstance(thresholds, (list, tuple))
            and len(thresholds) == 2
            and all(isinstance(item, (int, float)) for item in thresholds)
        ):
            raise TypeError(
                Errors.bad_input(
                    name="thresholds", expected_type="a tuple with two numericalw"
                )
            )
    if not isinstance(binarize, bool):
        raise TypeError(Errors.bad_input(name="binarize", expected_type="a boolean"))
    if not isinstance(as_array, bool):
        raise TypeError(Errors.bad_input(name="as_array", expected_type="a boolean"))

    result = spyndex.computeIndex([index_id], parameters)
    result = np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)

    if thresholds is not None:
        if binarize:
            mask = np.logical_and(result >= thresholds[0], result <= thresholds[1])
            result = np.where(mask, 1, 0)
        else:
            result = np.clip(result, thresholds[0], thresholds[1])

    if alpha is not None:
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
