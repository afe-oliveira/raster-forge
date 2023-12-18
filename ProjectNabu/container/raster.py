from typing import TypedDict

import numpy as np
import rasterio


class RasterImportConfig(TypedDict):
    id: int
    name: str
    min: int
    max: int


class Raster:

    __scale = None

    layers = {}
    transform = None
    projection = None

    def __init__(self, scale: int):
        self.__scale = scale

        self.layers = {}
        self.transform = None
        self.projection = None

    # ****************

    @property
    def scale(self):
        return self.__scale

    # ****************

    def import_layers(self, path: str, config: list[RasterImportConfig]):
        with rasterio.open(path) as dataset:
            for item in config:
                band = dataset.read(item["id"])
                band = np.interp(band, (band.min(), band.max()), (item['min'], item['max']))
                self.layers[item["name"]] = band.astype(np.uint8)

    def add_layer(self, data: np.ndarray, name: str):
        if name not in self.layers.keys():
            self.layers[name] = data

    def remove_layer(self, name: str):
        if name in self.layers.keys():
            self.layers.pop(name)
