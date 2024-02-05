from typing import Optional

import numpy as np
import spyndex


def index(
    index: str,
    parameters: dict,
    alpha: Optional[np.ndarray] = None,
    thresholds: Optional[tuple[float, float]] = None,
    binarize: bool = False,
) -> np.ndarray[np.float32]:
    result = spyndex.computeIndex([index], parameters)
    result = np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)

    if thresholds is not None:
        if binarize:
            mask = np.logical_and(result >= thresholds[0], result <= thresholds[1])
            result = np.where(mask, 1, 0)
        else:
            result = np.clip(result, thresholds[0], thresholds[1])

    if alpha is not None:
        result = np.dstack([result, alpha])

    return result
