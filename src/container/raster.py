from typing import TypedDict

import numpy as np
from osgeo import gdal


class RasterImportConfig(TypedDict):
    id: int
    name: str
    min: int
    max: int


class Raster:
    layers = {}

    transform = None
    projection = None

    def __init__(self):
        self.layers = {}
        self.transform = None
        self.projection = None

    def import_layers(self, path: str, config: list[RasterImportConfig]):
        dataset = gdal.Open(path, gdal.GA_ReadOnly)

        for item in config:
            band = dataset.GetRasterBand(item["id"]).ReadAsArray()
            band = np.clip(band, item["min"], item["max"])
            self.layers[item["name"]] = band

    def add_layer(self, data: np.ndarray, name: str):
        if name not in self.layers.keys():
            self.layers[name] = data

    def remove_layer(self, name: str):
        if name in self.layers.keys():
            self.layers.pop(name)
