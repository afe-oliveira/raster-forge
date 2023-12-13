import numpy as np


def rgb(red: np.ndarray, green: np.ndarray, blue: np.ndarray, alpha: np.ndarray = None, gamma: tuple[float, float, float] = None) -> np.ndarray:
    """Creates an RGB(A) array.

    Args:
      red:
        Red band data.
      green:
        Green band data.
      blue:
        Blue band data.
      alpha:
        Alpha band data.
      gamma:
        Gamma values to be applied to the red, green and blue bands, respectively.

    Returns:
      RGB(A) composite array.
    """
    result = np.dstack([red, green, blue])

    if gamma is not None:
        aux_result = np.zeros_like(result)
        aux_result[:, :, 2] = np.power(result[:, :, 0], gamma[0])
        aux_result[:, :, 1] = np.power(result[:, :, 1], gamma[1])
        aux_result[:, :, 0] = np.power(result[:, :, 2], gamma[2])

        result = (aux_result * 255.0 / np.max(aux_result)).astype(np.uint8)

    if alpha is not None:
        result = np.dstack([result, alpha])

    return result


def cir(nir: np.ndarray, red: np.ndarray, green: np.ndarray, alpha: np.ndarray = None) -> np.ndarray:
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
