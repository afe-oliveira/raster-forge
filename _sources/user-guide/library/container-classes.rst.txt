Using the Container Classes
===========================

All generation processes can directly utilize NumPy_ N-dimensional arrays as inputs. However, Raster Forge provides two container classes, :py:class:`Layer <rforge.library.containers.layer.Layer>` and :py:class:`Raster <rforge.library.containers.raster.Raster>`, primarily to streamline the management of metadata.

.. _NumPy: https://numpy.org/doc/stable/reference/arrays.ndarray.html

Import Single Layers
--------------------

.. code-block:: python

    from rforge import Layer

    file_path = 'file/path/example.tif'

    red = Layer()
    red.import_layer(file_path, 1, 1)

    blue = Layer()
    blue.import_layer(file_path, 2, 1)

    green = Layer()
    green.import_layer(file_path, 3, 1)

Import Layers in Bulk
---------------------

.. code-block:: python

    from rforge import Raster

    file_path = 'file/path/example.tif'

    raster = Raster(scale=1)
    layer_dict = [
        {"name": "red", "id": 1},
        {"name": "blue", "id": 2},
        {"name": "green", "id": 3},
    ]

    raster.import_layers(file_path, layer_dict)