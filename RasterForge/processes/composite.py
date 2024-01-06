from enum import Enum

import numpy as np

from RasterForge.containers.layer import Layer


class CompositeType(Enum):
    """Enumerates types of composite bands and their dispositions.
    """
    TRUE_COLOR = ['Red', 'Green', 'Blue']
    CIR = ['NIR', 'Red', 'Green']


def composite(layers: list[Layer], alpha: Layer = None, gamma: list[float] = None) -> Layer:
    """Stacks all provided layers into a single array in order. Applies gamma correction.

    Args:
      layers:
        List of raster layers.
      alpha:
        Alpha layer.
      gamma:
        List of gamma values.
    Returns:
      Stacked composite layer.
    """
    result = np.dstack([layer() for layer in layers])

    if gamma is not None:
        aux_result = np.zeros_like(result)
        for i in range(len(gamma)):
            aux_result[:, :, i] = np.power(result[:, :, i], gamma[i])

        # result = (aux_result * 255.0 / np.max(aux_result)).astype(np.uint8)

    if alpha is not None:
        result = np.dstack([result, alpha])

    return Layer(result)