from osgeo import gdal

class MapRaster:

    layers = {}

    transform = None
    projection = None

    def __init__(self, name, age):
        self.layers = {}
        self.transform = None
        self.projection = None

    def add_layers(self, path: str, names: list[str]):
        dataset = gdal.Open(path, gdal.GA_ReadOnly)

        for i in range(1, dataset.RasterCount + 1):
            band = dataset.GetRasterBand(i).ReadAsArray()
            self.layers[names[i - 1]] = band