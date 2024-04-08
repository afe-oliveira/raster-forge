import os
from typing import Dict, Optional, TypedDict, Union

import rasterio

from rforge.library.tools.rescale_dataset import rescale_dataset
from rforge.library.tools.exceptions import Errors

from rforge.library.containers.layer import Layer


class RasterImportConfig(TypedDict):
    id: int
    name: str


class Raster:
    """Represents a collection of layers in a geospatial dataset.

    Attributes:
        _layers (Dict[str, Layer]): Dictionary mapping layer names to Layer instances.
        _scale (int): The scale factor of the raster dataset.

    Methods:
        __init__: Initializes a Raster instance.
        __str__: Returns a string representation of the raster dataset.
        layers: Getter for the layers dictionary.
        count: Computes the number of layers in the dataset.
        scale: Getter for the scale factor.
        import_layers: Imports layers from a raster file.
        add_layer: Adds a layer to the raster dataset.
        remove_layer: Removes a layer from the raster dataset.
        edit_layer: Renames a layer in the raster dataset.
    """
    _layers: Dict[str, Layer]
    _scale: int

    def __init__(self, scale: int, layers: Optional[Dict[str, Layer]] = None):
        if not isinstance(scale, int) or (isinstance(scale, int) and scale <= 0):
            raise TypeError(
                Errors.bad_input(name="scale", expected_type="an integer larger than 0")
            )
        if layers is None:
            layers = {}
        else:
            if not isinstance(layers, dict):
                raise TypeError(
                    Errors.bad_input(name="layers", expected_type="a dictionary")
                )
            for key, value in layers.items():
                if not isinstance(key, str):
                    raise TypeError(
                        Errors.bad_input(name="layers keys", expected_type="strings")
                    )
                if not isinstance(value, Layer):
                    raise TypeError(
                        Errors.bad_input(name="layers values", expected_type="Layers")
                    )
        self._layers = layers
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

    def import_layers(
        self, path: str, config: Optional[list[Dict[str, Union[str, int]]]] = None
    ):
        if not os.path.exists(path):
            raise FileNotFoundError(Errors.file_not_found(file_path=path))

        with rasterio.open(path) as dataset:
            dataset = rescale_dataset(dataset, self.scale)

            if config is None:
                config = []
                for id in range(1, dataset.count + 1):
                    aux_config: Dict[str, Union[str, int]] = {"name": f"Layer {id}", "id": id}
                    config.append(aux_config)

            for item in config:
                array = dataset.read(item["id"])

                bounds = {
                    "left": dataset.bounds[0],
                    "bottom": dataset.bounds[1],
                    "right": dataset.bounds[2],
                    "top": dataset.bounds[3],
                }
                crs = (
                    str(dataset.crs.to_epsg())
                    if dataset.crs.to_epsg() is not None
                    else "4326"
                )
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
                units = dataset.units[int(item["id"]) - 1]

                layer = Layer(
                    array=array,
                    bounds=bounds,
                    crs=crs,
                    driver=driver,
                    no_data=no_data,
                    transform=transform,
                    units=units,
                )

                self._layers[str(item["name"])] = layer

    def add_layer(self, layer: Layer, name: str):
        if not isinstance(layer, Layer):
            raise TypeError(Errors.bad_input(name="layer", expected_type="a Layer"))
        if not isinstance(name, str):
            raise TypeError(
                Errors.bad_input(name="layer name", expected_type="a string")
            )
        if name not in self._layers.keys():
            self._layers[name] = layer

    def remove_layer(self, name: str):
        if not isinstance(name, str):
            raise TypeError(
                Errors.bad_input(name="layer name", expected_type="a string")
            )
        if name in self._layers.keys():
            self._layers.pop(name)

    def edit_layer(self, current_name: str, new_name: str):
        if not isinstance(current_name, str):
            raise TypeError(
                Errors.bad_input(name="current layer name", expected_type="a string")
            )
        if not isinstance(new_name, str):
            raise TypeError(
                Errors.bad_input(name="new layer name", expected_type="a string")
            )
        if current_name in self._layers.keys():
            self._layers[new_name] = self._layers.pop(current_name)
