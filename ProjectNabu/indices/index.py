from typing import Callable, Any, Union

import numpy as np


def index(formula: Callable[..., np.ndarray], alpha: np.ndarray, *variables: Union[np.ndarray, int, float]) -> np.ndarray[np.float32]:
    variables = [
        np.nan_to_num(var, nan=0.0, posinf=0.0, neginf=0.0) if isinstance(var, np.ndarray)
        else np.nan_to_num(var) for
        var in variables
    ]

    result = formula(*variables)
    result = (2 * (result - np.min(result)) / (np.max(result) - np.min(result))) - 1

    if alpha is not None:
        result = np.dstack([result, alpha])

    return result
