from typing import TypedDict

import numpy as np


class WeightedCompositeConfig(TypedDict):
    layer: np.ndarray
    weight: float


def stacked_composite(data: list[np.ndarray]) -> np.ndarray:
    """Stacks all provided layers into a single array in order.

    Args:
      data:
        List of process data layers.

    Returns:
      Stacked composite array.
    """
    result = np.dstack(data)

    return result


def weighted_composite(data: list[WeightedCompositeConfig]) -> np.ndarray:
    """Creates a weighted composite array based on provided layers and weights.

    Args:
      data:
        List of dictionaries containing process data with the format {layer: np.ndarray, weight: float}.

    Returns:
      Weighted composite array.
    """
    layers = [entry['layer'] for entry in data]
    weights = [entry['weight'] for entry in data]

    result = np.average(layers, axis=0, weights=weights)

    return result
