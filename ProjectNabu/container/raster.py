from typing import TypedDict, Union, Literal, Dict, Optional, Tuple

import numpy as np
import rasterio

from .layer import Layer


class RasterImportConfig(TypedDict):
    id: int
    name: str
    type: Literal['relative', 'absolute']


class Raster:

    _layers: Dict[str, Layer] = {}

    _scale: int = None
    _transform: Optional[Tuple[float, float, float, float, float, float]] = None
    _projection: Optional[str] = None

    def __init__(self, scale: int):
        self._scale = scale

    # ****************

    @property
    def layers(self) -> dict[str, Layer]:
        return self._layers

    @property
    def scale(self) -> int:
        return self._scale

    # ****************

    def import_layers(self, path: str, config: list[RasterImportConfig]):
        with rasterio.open(path) as dataset:
            for item in config:
                layer = Layer()

                # Get Band Data
                band = dataset.read(item["id"])
                if item['type'] == 'relative':
                    band = np.interp(band, (band.min(), band.max()), (0, 255))
                    layer.data = band.astype(np.uint8)
                elif item['type'] == 'absolute':
                    layer.data = band.astype(np.int32)

                # Get Metadata
                layer.metadata = dataset.meta.copy()

                # Get Projection
                layer.projection = dataset.crs.to_string()

                # Get Transform
                layer.transform = dataset.transform

                # Save Layer
                self.layers[item["name"]] = layer

    def add_layer(self, layer: Layer, name: str):
        if name not in self.layers.keys():
            self.layers[name] = layer

    def remove_layer(self, name: str):
        if name in self.layers.keys():
            self.layers.pop(name)

    def edit_layer(self, current_name: str, new_name: str):
        if current_name in self.layers.keys():
            self.layers[new_name] = self.layers.pop(current_name)
