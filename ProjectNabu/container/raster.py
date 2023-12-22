from typing import TypedDict, Union, Literal, Dict, Optional, Tuple

import numpy as np
import rasterio


class RasterImportConfig(TypedDict):
    id: int
    name: str
    type: Literal['relative', 'absolute']


class LayerFormat(TypedDict):
    data: np.ndarray[Union[np.uint8, np.int32]]
    type: Literal['relative', 'absolute']


class Raster:

    _layers: Dict[str, np.ndarray[Union[np.uint8, np.int32]]] = {}

    _scale: int = None
    _transform: Optional[Tuple[float, float, float, float, float, float]] = None
    _projection: Optional[str] = None

    def __init__(self, scale: int):
        self._scale = scale

    # ****************

    @property
    def layers(self) -> Dict[str, np.ndarray[Union[np.uint8, np.int32]]]:
        return self._layers

    @property
    def scale(self) -> int:
        return self._scale

    @property
    def transform(self) -> Optional[Tuple[float, float, float, float, float, float]]:
        return self._transform

    @transform.setter
    def transform(self, value: Optional[Tuple[float, float, float, float, float, float]]):
        self._transform = value

    @property
    def projection(self) -> Optional[str]:
        return self._projection

    @projection.setter
    def projection(self, value: Optional[str]):
        self._projection = value

    # ****************

    def import_layers(self, path: str, config: list[RasterImportConfig]):
        with rasterio.open(path) as dataset:
            for item in config:
                band = dataset.read(item["id"])

                if item['type'] == 'relative':
                    band = np.interp(band, (band.min(), band.max()), (0, 255))
                    self.layers[item["name"]] = band.astype(np.uint8)
                elif item['type'] == 'absolute':
                    self.layers[item["name"]] = band.astype(np.int32)

    def add_layer(self, data: np.ndarray, name: str):
        if name not in self.layers.keys():
            self.layers[name] = data

    def remove_layer(self, name: str):
        if name in self.layers.keys():
            self.layers.pop(name)

    def edit_layer(self, current_name: str, new_name: str):
        if current_name in self.layers.keys():
            self.layers[new_name] = self.layers.pop(current_name)

    # ****************

    def import_transform(self, path: str):
        with rasterio.open(path) as dataset:
            self.transform = dataset.transform

    def import_projection(self, path: str):
        with rasterio.open(path) as dataset:
            self.projection = dataset.crs.to_string()

    def import_metadata(self, path: str):
        with rasterio.open(path) as dataset:
            self.metadata = dataset.meta.copy()
