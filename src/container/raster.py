import numpy as np
from osgeo import gdal

CONFIG_SCHEMA = {'id': int, 'name': str, 'min': int, 'max': int}


class Raster:

    layers = {}

    transform = None
    projection = None

    def __init__(self, name, age):
        self.layers = {}
        self.transform = None
        self.projection = None

    def add_layers(self, path: str, config: list[dict]):
        dataset = gdal.Open(path, gdal.GA_ReadOnly)

        for item in config:

            if set(list(CONFIG_SCHEMA.keys())) != set(item.keys()):
                raise KeyError('Import configuration keys are not correct.')

            for key, type_id in CONFIG_SCHEMA.items():
                if not isinstance(item[key], type_id):
                    raise TypeError('{0} must be {1}'.format(key, type_id))

            band = dataset.GetRasterBand(item['id']).ReadAsArray()
            band = np.clip(band, item['min'], item['max'])
            self.layers[item['name']] = band
