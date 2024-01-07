from typing import Callable

import numpy as np


def sr() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: nir / red


def ndvi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: np.where((nir + red) == 0, 0, (nir - red) / (nir + red))


def dvi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: nir - red


def rdvi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: (nir - red) / np.sqrt(nir + red)


def msr() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: ((nir / red - 1) / np.sqrt(nir / red + 1))


def gndvi() -> Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, green, red: (nir - green) / (nir + green)


def gari() -> Callable[[np.ndarray, np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, green, blue, red: (
        (nir - green - 1.7 * (blue - red)) / (nir + green - 1.7 * (blue - red))
    )


def idvi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: ((1 + nir - red) / (1 - nir - red))


def ndre() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red_edge: (nir - red_edge) / (nir + red_edge)


def dvi2() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, green: nir - green


def grvi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, green: nir / green


def ndwi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda green, nir: (green - nir) / (green + nir)


def ari() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda green, red_edge: (1 / green - 1 / red_edge)


def mari() -> Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    return lambda green, red_edge, red: ((1 / green - 1 / red_edge) * red)


def evi() -> Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red, blue: (2.5 * (nir - red)) / (nir + 6 * red - 7.5 * blue + 1)


def evi2() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: (2.5 * (nir - red)) / (nir + 2.4 * red + 1)


def savi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: (1.5 * (nir - red) / (nir + red + 0.5))


def msavi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: (1.5 * (nir - red) / (nir + red + 0.5))


def osavi() -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red: (1.5 * (nir - red) / (nir + red + 0.5))


def tavi() -> Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red, blue: ((nir + 2.280 * np.max(red) - red) / red)


def rei() -> Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    return lambda nir, red, blue: (nir - red) / (nir + (blue * red))
