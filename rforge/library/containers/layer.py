import os
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import rasterio
from rforge.library.tools.exceptions import Errors
from rforge.library.tools.rescale_dataset import rescale_dataset

ERROR_MESSAGES = {
    "no_file": "Error: The file {file_path} does not exist.",
    "array": "ERROR: 'array' argument is {array_type}, but it must be a NumPy array of numeric type.",
    "bounds_type": (
        "ERROR: 'bounds' argument is {bounds_type}, but it must be a dictionary."
    ),
    "bounds_values": "ERROR: All values in 'bounds' must be numeric.",
    "bounds_keys": "ERROR: 'bounds' argument has keys {bounds_keys}, but must contain the keys {{'left', 'bottom', 'right', 'top'}}.",
    "crs": "ERROR: 'crs' argument is {crs_type}, but it must be a string.",
    "driver": "ERROR: 'driver' argument is {driver_type}, but it must be a string.",
    "no_data": "ERROR: 'no_data' argument is {no_data_type}, but it must be an integer or float.",
    "transform": "ERROR: 'transform' argument is {transform_type}, but it must be a tuple of six floats.",
    "units": "ERROR: 'units' argument is {units_type}, but it must be a string.",
}


class Layer:
    """Represents a data layer in a geospatial dataset.

    Attributes:
        _array (Optional[np.ndarray[np.int32]]): The array data of the layer.
        _bounds (Optional[Dict[str, float]]): The spatial bounds of the layer.
        _crs (Optional[str]): The coordinate reference system (CRS) of the layer.
        _driver (Optional[str]): The driver used for data storage.
        _no_data (Optional[Union[int, float]]): The value representing no data in the layer.
        _transform (Optional[Tuple[float, float, float, float, float, float]]): Affine transformation parameters.
        _units (Optional[str]): The units of the layer data.

    Methods:
        __init__: Initializes a Layer instance.
        __eq__: Checks equality between two Layer instances or a Layer and a numpy array.
        __str__: Returns a string representation of the layer attributes.
        import_layer: Imports layer data from a file.
        array: Getter and setter for the layer array data.
        bounds: Getter and setter for the spatial bounds.
        crs: Getter and setter for the CRS.
        driver: Getter and setter for the driver.
        no_data: Getter and setter for the no_data value.
        transform: Getter and setter for the affine transformation parameters.
        units: Getter and setter for the units.
        resolution: Computes the resolution of the layer.
        width: Computes the width of the layer.
        height: Computes the height of the layer.
        count: Computes the number of bands in the layer.
        mean: Computes the mean value(s) of the layer data.
        median: Computes the median value(s) of the layer data.
        min: Computes the minimum value(s) of the layer data.
        max: Computes the maximum value(s) of the layer data.
        std_dev: Computes the standard deviation value(s) of the layer data.
    """

    _array: Optional[np.ndarray[Union[np.uint8, np.int32]]] = None

    _bounds: Optional[Dict[str, float]] = None
    _crs: Optional[str] = None
    _driver: Optional[str] = None
    _no_data: Optional[Union[int, float]] = None
    _transform: Optional[Tuple[float, float, float, float, float, float]] = None
    _units: Optional[str] = None

    def __init__(
        self,
        array: Optional[np.ndarray[np.int32]] = None,
        bounds: Optional[Dict[str, Union[float, int]]] = None,
        crs: Optional[str] = None,
        driver: Optional[str] = None,
        no_data: Optional[Union[int, float]] = None,
        transform: Optional[Tuple[float, float, float, float, float, float]] = None,
        units: Optional[str] = None,
    ):
        if array is not None and not (
            isinstance(array, np.ndarray) and np.issubdtype(array.dtype, np.number)
        ):
            raise TypeError(
                Errors.bad_input(
                    name="array",
                    provided_type=type(array),
                    expected_type="a numeric array",
                )
            )

        if bounds is not None:
            if not isinstance(bounds, dict):
                raise TypeError(
                    Errors.bad_input(
                        name="bounds",
                        provided_type=type(bounds),
                        expected_type="a dictionary",
                    )
                )
            if not all(isinstance(value, (int, float)) for value in bounds.values()):
                raise TypeError(ERROR_MESSAGES["bounds_values"])
            if not (set(bounds.keys()) == {"left", "bottom", "right", "top"}):
                raise TypeError(
                    ERROR_MESSAGES["bounds_keys"].format(bounds_keys=set(bounds.keys()))
                )

        if crs is not None and not isinstance(crs, str):
            raise TypeError(ERROR_MESSAGES["crs"].format(crs_type=type(crs)))

        if driver is not None and not isinstance(driver, str):
            raise TypeError(ERROR_MESSAGES["driver"].format(driver_type=type(driver)))

        if no_data is not None and not isinstance(no_data, (int, float)):
            raise TypeError(
                ERROR_MESSAGES["no_data"].format(no_data_type=type(no_data))
            )

        if transform is not None and not (
            isinstance(transform, tuple)
            and len(transform) == 6
            and all((isinstance(value, (int, float)) for value in transform))
        ):
            raise TypeError(
                ERROR_MESSAGES["transform"].format(transform_type=type(transform))
            )

        if units is not None and not isinstance(units, str):
            raise TypeError(ERROR_MESSAGES["units"].format(units_type=type(units)))

        self._array = array
        self._bounds = bounds
        self._crs = crs
        self._driver = driver
        self._no_data = no_data
        self._transform = transform
        self._units = units

    def __eq__(self, other):
        if isinstance(other, Layer):
            return (
                np.allclose(self._array, other.array, atol=0.01)
                and self._bounds == other.bounds
                and self._crs == other.crs
                and self._driver == other.driver
                and self._no_data == other.no_data
                and self._transform == other.transform
                and self._units == other.units
            )
        elif isinstance(other, np.ndarray):
            return (
                np.allclose(self._array, other, atol=0.01)
                and self.width == other.shape[1]
                and self.height == other.shape[0]
                and self.count == (other.shape[2] if len(other.shape) == 3 else 1)
            )
        else:
            return False

    def __str__(self) -> str:
        return str(
            {
                "crs": self.crs,
                "driver": self.driver,
                "bounds": self.bounds,
                "no_data": self.no_data,
                "transform": self.transform,
                "units": self.units,
                "resolution": self.resolution,
                "width": self.width,
                "height": self.height,
                "count": self.count,
                "mean": self.mean,
                "median": self.median,
                "minimum": self.min,
                "maximum": self.max,
                "standard_deviation": self.std_dev,
            }
        )

    def import_layer(self, path: str, id: int = 1, scale: Optional[int] = None):
        if not os.path.exists(path):
            raise FileNotFoundError(ERROR_MESSAGES["no_file"].format(file_path=path))

        with rasterio.open(path) as dataset:
            if scale is not None:
                dataset = rescale_dataset(dataset, scale)

            array = dataset.read(id)

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
            units = dataset.units[id - 1]

            self.array = array

            self.bounds = bounds
            self.crs = crs
            self.driver = driver
            self.no_data = no_data
            self.transform = transform
            self.units = units

    @property
    def array(self) -> Optional[np.ndarray[np.int32]]:
        return self._array

    @array.setter
    def array(self, value: np.ndarray[np.int32]):
        if value is not None and not (
            isinstance(value, np.ndarray) and np.issubdtype(value.dtype, np.number)
        ):
            raise TypeError(ERROR_MESSAGES["array"].format(array_type=type(value)))
        self._array = value

    @property
    def bounds(self) -> Optional[Dict[str, float]]:
        return self._bounds

    @bounds.setter
    def bounds(self, value: Dict[str, float]):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError(
                    ERROR_MESSAGES["bounds_type"].format(bounds_type=type(value))
                )
            if not all(isinstance(value, (int, float)) for value in value.values()):
                raise TypeError(ERROR_MESSAGES["bounds_values"])
            if not (set(value.keys()) == {"left", "bottom", "right", "top"}):
                raise TypeError(
                    ERROR_MESSAGES["bounds_keys"].format(bounds_keys=set(value.keys()))
                )
        self._bounds = value

    @property
    def crs(self) -> Optional[str]:
        return self._crs

    @crs.setter
    def crs(self, value: str):
        if value is not None and not isinstance(value, str):
            raise TypeError(ERROR_MESSAGES["crs"].format(crs_type=type(value)))
        self._crs = value

    @property
    def driver(self) -> Optional[str]:
        return self._driver

    @driver.setter
    def driver(self, value: str):
        if value is not None and not isinstance(value, str):
            raise TypeError(ERROR_MESSAGES["driver"].format(driver_type=type(value)))
        self._driver = value

    @property
    def no_data(self) -> Optional[Union[int, float]]:
        return self._no_data

    @no_data.setter
    def no_data(self, value: Union[int, float]):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(ERROR_MESSAGES["no_data"].format(no_data_type=type(value)))
        self._no_data = value

    @property
    def transform(self) -> Optional[Tuple[float, float, float, float, float, float]]:
        return self._transform

    @transform.setter
    def transform(self, value: Tuple[float, float, float, float, float, float]):
        if value is not None and not (
            isinstance(value, tuple)
            and len(value) == 6
            and all((isinstance(v, (int, float)) for v in value))
        ):
            raise TypeError(
                ERROR_MESSAGES["transform"].format(transform_type=type(value))
            )
        self._transform = value

    @property
    def units(self) -> Optional[str]:
        return self._units

    @units.setter
    def units(self, value: str):
        if value is not None and not isinstance(value, str):
            raise TypeError(ERROR_MESSAGES["units"].format(units_type=type(value)))
        self._units = value

    @property
    def resolution(self) -> float:
        if self._array is not None and self._transform is not None:
            return self._transform[1]
        else:
            return 0

    @property
    def width(self) -> int:
        if self._array is not None:
            return self._array.shape[1]
        else:
            return 0

    @property
    def height(self) -> int:
        if self._array is not None:
            return self._array.shape[0]
        else:
            return 0

    @property
    def count(self) -> int:
        if self._array is not None:
            return self._array.shape[2] if len(self._array.shape) == 3 else 1
        else:
            return 0

    @property
    def mean(self) -> Optional[Union[float, int, list[Union[int, float]]]]:
        if self._array is not None:
            return (
                float(np.mean(self._array))
                if len(self._array.shape) <= 2
                else [
                    float(np.mean(self._array[:, :, i]))
                    for i in range(self._array.shape[2])
                ]
            )
        else:
            return None

    @property
    def median(self) -> Optional[Union[float, int, list[Union[int, float]]]]:
        if self._array is not None:
            return (
                float(np.median(self._array))
                if len(self._array.shape) <= 2
                else [
                    float(np.median(self._array[:, :, i]))
                    for i in range(self._array.shape[2])
                ]
            )
        else:
            return None

    @property
    def min(self) -> Optional[Union[float, int, list[Union[int, float]]]]:
        if self._array is not None:
            return (
                float(np.min(self._array))
                if len(self._array.shape) <= 2
                else [
                    float(np.min(self._array[:, :, i]))
                    for i in range(self._array.shape[2])
                ]
            )
        else:
            return None

    @property
    def max(self) -> Optional[Union[float, int, list[Union[int, float]]]]:
        if self._array is not None:
            return (
                float(np.max(self._array))
                if len(self._array.shape) <= 2
                else [
                    float(np.max(self._array[:, :, i]))
                    for i in range(self._array.shape[2])
                ]
            )
        else:
            return None

    @property
    def std_dev(self) -> Optional[Union[float, int, list[Union[int, float]]]]:
        if self._array is not None:
            return (
                float(np.std(self._array))
                if len(self._array.shape) <= 2
                else [
                    float(np.std(self._array[:, :, i]))
                    for i in range(self._array.shape[2])
                ]
            )
        else:
            return None
