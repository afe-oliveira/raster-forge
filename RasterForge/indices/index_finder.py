import sys
from typing import Callable

import numpy as np


def _find_indices() -> dict[str, Callable[..., np.ndarray]]:
    """Find multi-spectral index functions registered as plugins.

    Returns:
      A dictionary containing the found multi-spectral index functions.
    """
    if sys.version_info < (3, 10):
        from importlib_metadata import entry_points
    else:
        from importlib.metadata import entry_points

    plugin_entrypoints = entry_points(group="index.base")

    return {ep.name: ep.load() for ep in plugin_entrypoints}
