from typing import Dict, Optional, TypedDict

import rasterio

from RasterForge.tools.rescale_dataset import rescale_dataset

from .layer import Layer

from tqdm import tqdm

ERROR_MESSAGES = {
    "scale": "ERROR: 'scale' argument is {scale_type}, but it must be an integer."
}


class RasterImportConfig(TypedDict):
    id: int
    name: str


class Raster:
    _layers: Dict[str, Layer] = {}
    _scale: int = None

    def __init__(self, scale: int):
        if not isinstance(scale, int):
            raise TypeError(ERROR_MESSAGES["scale"].format(units_type=type(scale)))
        self._scale = scale

    def __str__(self):
        return str({key: value.__str__() for key, value in self._layers.items()})

    @property
    def layers(self) -> Dict[str, Layer]:
        return self._layers

    @property
    def count(self) -> int:
        return len(self._layers)

    @property
    def scale(self) -> int:
        return self._scale

    def import_layers(self, path: str, config: Optional[list[RasterImportConfig]] = None):
        with rasterio.open(path) as dataset:
            dataset = rescale_dataset(dataset, self.scale)

            if config is None:
                config = []
                for id in range(1, dataset.count + 1):
                    aux_config = {}
                    aux_config['name'] = f"Layer {id}"
                    aux_config['id'] = id
                    config.append(aux_config)

            for i, item in enumerate(tqdm(config)):
                array = dataset.read(item["id"])

                bounds = {
                    "left": dataset.bounds[0],
                    "bottom": dataset.bounds[1],
                    "right": dataset.bounds[2],
                    "top": dataset.bounds[3],
                }
                crs = str(dataset.crs)
                driver = dataset.meta["driver"].upper()
                no_data = dataset.nodata
                transform = (
                    dataset.transform.c,
                    dataset.transform.a,
                    dataset.transform.b,
                    dataset.transform.f,
                    dataset.transform.d,
                    dataset.transform.e,
                )
                units = dataset.units[item["id"] - 1]

                layer = Layer(
                    array=array,
                    bounds=bounds,
                    crs=crs,
                    driver=driver,
                    no_data=no_data,
                    transform=transform,
                    units=units,
                )

                self._layers[item["name"]] = layer

    def add_layer(self, layer: Layer, name: str):
        if name not in self._layers.keys():
            self._layers[name] = layer

    def remove_layer(self, name: str):
        if name in self._layers.keys():
            self._layers.pop(name)

    def edit_layer(self, current_name: str, new_name: str):
        if current_name in self._layers.keys():
            self._layers[new_name] = self._layers.pop(current_name)
