import numpy as np


def _cir(nir: np.ndarray, red: np.ndarray, green: np.ndarray, alpha: np.ndarray = None) -> np.ndarray:
    """Creates an RGB(A) array.

    Args:
      nir:
        Near-infrared band data.
      red:
        Red band data.
      green:
        Green band data.
      alpha:
        Alpha band data.

    Returns:
      RGB(A) composite array.
    """
    result = np.dstack([nir, red, green])
    if alpha is not None:
        result = np.dstack([result, alpha])

    return result
