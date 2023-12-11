from typing import Callable, Any, Union

import numpy as np


def index(formula: Callable[..., np.ndarray], *variables: Union[np.ndarray, int, float]) -> np.ndarray[np.float32]:
    result = formula(*variables)
    result = (2 * (result - np.min(result)) / (np.max(result) - np.min(result))) - 1

    return result
