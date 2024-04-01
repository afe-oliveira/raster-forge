Developement
============

Installing Development Version
------------------------------

- On Windows

.. code-block:: bash

   git clone https://github.com/afe-oliveira/raster-forge
   cd raster-forge
   python -m venv env
   . env\Scripts\activate
   pip install -e .[dev]

- Other OS

.. code-block:: bash

   git clone https://github.com/afe-oliveira/raster-forge
   cd raster-forge
   python -m venv env
   source env/bin/activate
   pip install -e .[dev]

Run Tests
---------

The project utilizes the PyTest_ testing architecture. To run the tests, execute the following command:

.. code-block:: bash

   pytest

If you want to generate a code coverage report, execute the command:

.. code-block:: bash

   pytest --cov=parshift --cov-report=html

After, navigate to ``htmlcov/index.html`` and open the generated HTML report in your preferred web browser. This will provide you with a detailed overview of the coverage analysis in a user-friendly format.

Building Documentation
----------------------

In the `raster-forge` project folder, execute the command:

.. code-block:: bash

    sphinx-build docs docs/_build

The generated documentation will be placed in `docs/_build`.

Code Styling
------------

Raster Forge source code follows the Black_ style.

.. _PyTest: https://docs.pytest.org
.. _Black: https://black.readthedocs.io/en/stable/