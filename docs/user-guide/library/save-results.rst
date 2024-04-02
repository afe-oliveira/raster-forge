Saving Results
==============

The :py:class:`Layer <rforge.library.containers.layer.Layer>` data is stored within inner NumPy_ N-dimensional arrays. Therefore, we can utilize any conventional method to save it. In this particular example, we employ the tifffile_ package.

.. _NumPy: https://numpy.org/doc/stable/reference/arrays.ndarray.html
.. _tifffile: https://pypi.org/project/tifffile/

.. code-block:: python

    from rforge import Raster
    from rforge import composite

    import tifffile

Generating Composite
--------------------

.. code-block:: python

    file_path = 'file/path/example.tif'

    raster = Raster(scale=1)
    layer_dict = [
        {'name': 'red', 'id': 1},
        {'name': 'blue', 'id': 2},
        {'name': 'green', 'id': 3},
        {'name': 'alpha', 'id': 4},
    ]
    raster.import_layers(file_path, layer_dict)

    layers = [raster.layers['red'], raster.layers['green'], raster.layers['blue']]
    gamma = [1, 1, 1]

    composite_layer = composite(layers=layers, alpha=raster.layers['alpha'], gamma=gamma)
    raster.add_layer(layer=composite_layer, name='rgb')

Saving Layers
-------------

.. code-block:: python

    tifffile.imwrite('file/path/example/red.tif', raster.layers['red'].array)
    tifffile.imwrite('file/path/example/blue.tif', raster.layers['blue'].array)
    tifffile.imwrite('file/path/example/green.tif', raster.layers['green'].array)

Saving Composite
----------------

.. code-block:: python

    tifffile.imwrite('file/path/example/rgb.tif', raster.layers['rgb'].array)