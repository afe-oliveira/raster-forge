import sys
from typing import Callable

import numpy as np


def _find_composites() -> dict[str, Callable[..., np.ndarray]]:
    """Find composite functions registered as plugins.

        Returns:
          A dictionary containing the found composite functions.
    """
    if sys.version_info < (3, 10):
        from importlib_metadata import entry_points
    else:
        from importlib.metadata import entry_points

    plugin_entrypoints = entry_points(group="composite.basic")

    return {ep.name: ep.load() for ep in plugin_entrypoints}