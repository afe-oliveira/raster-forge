Installation
============

Requirements
------------

**Python 3.9+**

A. Library

- NumPy_
- Rasterio_
- Spyndex_
- OpenCV_
- Dask_

.. _NumPy: https://pypi.org/project/numpy/
.. _Rasterio: https://pypi.org/project/rasterio/
.. _Spyndex: https://pypi.org/project/spyndex/
.. _OpenCV: https://pypi.org/project/opencv-python/
.. _Dask: https://pypi.org/project/dask/

B. GUI

- Matplotlib_
- PySide6_

.. _Matplotlib: https://pypi.org/project/matplotlib/
.. _PySide6: https://pypi.org/project/PySide6/

PyPi Instalation
----------------

The recommended method for installing RasterForge is via pip, the Python package manager. Simply run the following command:

.. code-block:: bash

    pip install raster-forge

This will download and install the latest version of Raster Forge. **If you intend to utilize the graphic user interface** (GUI) component of Raster Forge, ensure that the GUI dependencies are installed using the following command instead:

.. code-block:: bash

    pip install raster-forge[gui]

Source Instalation
------------------

If you prefer to install RasterForge from source, you can clone the repository from GitHub_ and install it manually:

.. code-block:: bash

    cd raster-forge
    pip install .

Similarly, to install the GUI component, the dependency needs to be indicated on installation:

.. code-block:: bash

    cd raster-forge
    pip install .[gui]

.. _GitHub: https://github.com/afe-oliveira/raster-forge