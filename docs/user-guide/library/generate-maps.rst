Generating Maps
===============

.. code-block:: python

    from rforge import Raster
    from rforge import composite, index, slope, aspect, distance, height, fuel

Importing Layer Data
--------------------

The initial step in every algorithm is data loading. Here, we utilize the container classes provided by Raster Forge.

.. code-block:: python

    file_path = 'file/path/example.tif'

    raster = Raster(scale=1)
    layer_dict = [
        {'name': 'red', 'id': 1},
        {'name': 'blue', 'id': 2},
        {'name': 'green', 'id': 3},
        {'name': 'nir', 'id': 4},
        {'name': 'dsm', 'id': 5},
        {'name': 'dtm', 'id': 6},
        {'name': 'alpha', 'id': 7},
    ]
    raster.import_layers(file_path, layer_dict)

Creating Composites
-------------------

Here we employ the :py:meth:`composite <rforge.lib.processes.composite>` function to generate a true color composite:

.. code-block:: python

    layers = [raster.layers['red'], raster.layers['green'], raster.layers['blue']]
    gamma = [1, 1, 1]

    composite_layer = composite(layers=layers, alpha=raster.layers['alpha'], gamma=gamma)
    raster.add_layer(layer=composite_layer, name='rgb')

In the above example, the result is returned as a :py:class:`Layer <rforge.lib.containers.layer.Layer>` and added to the :py:class:`Raster <rforge.lib.containers.raster.Raster>` collection. However, it is also possible to directly receive just a NumPy_ N-dimentional array.

.. _NumPy: https://numpy.org/doc/stable/reference/arrays.ndarray.html

.. code-block:: python

    composite_array = composite(
        layers=layers, alpha=raster.layers['alpha'], gamma=gamma, as_array=True
    )

Generating Multipsectral Index
------------------------------
The :py:meth:`index <rforge.lib.processes.index>` fuction draws on arguments sourced from the Spyndex_ package. Specifically, it utilizes the same indices identifiers and the parameter dictionary structure. The :py:meth:index <rforge.lib.processes.index> function facilitates index thresholding, enabling the retention of only the pertinent data, while also offering the capability to convert the resultant data into a binary mask for subsequent processing.

.. _Spyndex: https://spyndex.readthedocs.io/en/latest/

.. code-block:: python

    parameters_dict = {'N': raster.layers['nir'], 'R': raster.layers['red']}

* Simple

.. code-block:: python

    index_layer = index(
        index_id='NDVI', parameters=parameters_dict, alpha=raster.layers['alpha']
    )
    raster.add_layer(layer=index_layer, name='ndvi')

* Only Vegetation Data

.. code-block:: python

    vegetation_layer = index(
        index_id='NDVI',
        parameters=parameters_dict,
        alpha=raster.layers['alpha'],
        thresholds=[0, 1],
    )
    raster.add_layer(layer=vegetation_layer, name='vegetation')

* Vegetation Mask (Binary)

.. code-block:: python

    vegetation_binary_mask_layer = index(
        index_id='NDVI',
        parameters=parameters_dict,
        alpha=raster.layers['alpha'],
        thresholds=[0.25, 0.75],
        binarize=True,
    )
    raster.add_layer(layer=vegetation_binary_mask_layer, name='vegetation mask')

Other Processes
---------------

.. code-block:: python

    slope_layer = slope(
        dem=raster.layers['dtm'], units='degrees', alpha=raster.layers['alpha']
    )
    raster.add_layer(layer=slope_layer, name='slope')

    aspect_layer = aspect(
        dem=raster.layers['dtm'], units='degrees', alpha=raster.layers['alpha']
    )
    raster.add_layer(layer=aspect_layer, name='aspect')

.. code-block:: python

    distance_layer = distance(
        layer=raster.layers['vegetation mask'], alpha=raster.layers['alpha']
    )
    raster.add_layer(layer=distance_layer, name='distance')

.. code-block:: python

    height_layer = height(
        dtm=raster.layers['dtm'], dsm=raster.layers['dsm'], alpha=raster.layers['alpha']
    )
    raster.add_layer(layer=height_layer, name='canopy height')

.. code-block:: python

    fuel_layer = fuel(
        coverage=raster.layers['vegetation'],
        height=raster.layers['canopy height'],
        alpha=raster.layers['alpha'],
    )
    raster.add_layer(layer=height_layer, name='canopy height')
