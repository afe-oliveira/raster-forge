from typing import Callable

import numpy as np


def ndvi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: (nir - red) / (nir + red)
