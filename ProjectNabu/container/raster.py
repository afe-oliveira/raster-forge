from typing import TypedDict, Union, Literal, Dict, Optional, Tuple

import numpy as np
import rasterio
from rasterio import MemoryFile
from rasterio.enums import Resampling

from .layer import Layer


class RasterImportConfig(TypedDict):
    id: int
    name: str
    type: Literal['relative', 'absolute']


class Raster:

    _layers: Dict[str, Layer] = {}
    _scale: int = None

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
            dataset = self.rescale_dataset(dataset, self.scale)

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
                layer.metadata = dataset.meta

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

    # ****************

    def rescale_dataset(self, dataset, new_pixel_size):
        # Calculate Resampling Factors
        resampling_factor_x = dataset.res[0] / new_pixel_size
        resampling_factor_y = dataset.res[1] / new_pixel_size

        # Compute the New Transform Matrix
        new_transform = dataset.transform * rasterio.Affine.scale(resampling_factor_x, resampling_factor_y)

        # Update the Metadata with the new Transform and Resampling
        new_meta = dataset.meta.copy()
        new_meta.update({
            'transform': new_transform,
            'width': int(dataset.width * resampling_factor_x),
            'height': int(dataset.height * resampling_factor_y)
        })

        # Create an empty array for the rescaled data
        rescaled_data = np.empty((dataset.count, new_meta['height'], new_meta['width']), dtype=dataset.dtypes[0])

        # Read the rescaled data using the new transform and metadata
        dataset.read(out=rescaled_data, resampling=Resampling.bilinear)

        # Create a new dataset with the rescaled data and updated metadata
        rescaled_dataset = MemoryFile().open(
            driver='GTiff',
            count=dataset.count,
            dtype=dataset.dtypes[0],  # Assuming all bands have the same dtype
            width=new_meta['width'],
            height=new_meta['height'],
            transform=new_meta['transform'],
            crs=dataset.crs
        )

        rescaled_dataset.write(rescaled_data)

        return rescaled_dataset


