import numpy as np

class Index:
    def __init__(self, plugins:list=[]):
        pass

    def run(self):
        pass
def ndvi(
    nir: np.ndarray[np.float32], red: np.ndarray[np.float32]
) -> np.ndarray[np.float32]:
    index = (nir - red) / (nir + red)

    min_value = np.min(index)
    max_value = np.max(index)
    index = (2 * (index - min_value) / (max_value - min_value)) - 1

    return index
