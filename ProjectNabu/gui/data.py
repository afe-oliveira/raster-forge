from ProjectNabu.container.raster import Raster

"""
in_file = 'local_in/orthophoto.tif'
import_config = [{'id': 3, 'name': 'red', 'min': 0, 'max': 254},
                 {'id': 2, 'name': 'blue', 'min': 0, 'max': 254},
                 {'id': 1, 'name': 'green', 'min': 0, 'max': 254},
                 {'id': 4, 'name': 'nir', 'min': 0, 'max': 254},
                 {'id': 5, 'name': 'red_edge', 'min': 0, 'max': 254},
                 {'id': 6, 'name': 'alpha', 'min': 0, 'max': 254}]
"""
layer_data = Raster(1)
#layer_data.import_layers(in_file, import_config)