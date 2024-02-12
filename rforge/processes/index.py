from typing import Optional

import numpy as np
import spyndex
from rforge.containers.layer import Layer
from rforge.tools.data_validation import check_layer


def index(
    index: str,
    parameters: dict,
    alpha: Optional[np.ndarray] = None,
    thresholds: Optional[tuple[float, float]] = None,
    binarize: bool = False,
    as_array: bool = False,
) -> np.ndarray[np.float32]:
    for key, value in parameters.items():
        aux_value = check_layer(value)
        parameters[key] = aux_value

    result = spyndex.computeIndex([index], parameters)
    result = np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)

    if thresholds is not None:
        if binarize:
            mask = np.logical_and(result >= thresholds[0], result <= thresholds[1])
            result = np.where(mask, 1, 0)
        else:
            result = np.clip(result, thresholds[0], thresholds[1])

    if alpha is not None:
        alpha = check_layer(alpha)
        result = np.dstack([result, alpha])

    return result if as_array else Layer(result)
