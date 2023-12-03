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

    def __init__(self, name, age):
        self.layers = {}
        self.transform = None
        self.projection = None

    def import_layers(self, path: str, config: list[RasterImportConfig]):
        dataset = gdal.Open(path, gdal.GA_ReadOnly)

        for item in config:

            band = dataset.GetRasterBand(item['id']).ReadAsArray()
            band = np.clip(band, item['min'], item['max'])
            self.layers[item['name']] = band
