from typing import Union, Dict, Optional, Tuple, List

import numpy as np


class Layer:

    _array: Optional[np.ndarray[Union[np.uint8, np.int32]]] = None

    _bounds: Optional[Dict[str, float]] = None
    _crs: Optional[str] = None
    _driver: Optional[str] = None
    _no_data: Optional[Union[int, float]] = None
    _res: Optional[Dict[str,float]] = None
    _transform: Optional[Tuple[float, float, float, float, float, float]] = None
    _units: Optional[str] = None

    def __init__(
        self,
        array: np.ndarray[np.int32],
        bounds: Optional[Dict[str, float]] = None,
        crs: Optional[str] = None,
        driver: Optional[str] = None,
        no_data: Optional[Union[int, float]] = None,
        transform: Optional[Tuple[float, float, float, float, float, float]] = None,
        units: Optional[str] = None
    ):

        if not (isinstance(array, np.ndarray) and np.issubdtype(array.dtype, np.number)):
            raise TypeError(f"ERROR: 'array' argument is {type(array)}, but it must be a NumPy array of numeric type.")

        if bounds is not None:
            if not isinstance(bounds, dict):
                raise TypeError("ERROR: 'bounds' argument is {type(bounds)}, but it must be a dictionary.")
            if not all(isinstance(value, (int, float)) for value in bounds.values()):
                raise TypeError(f"ERROR: All values in 'bounds' must be numeric.")
            if not (set(bounds.keys()) == {'left', 'bottom', 'right', 'top'}):
                raise TypeError(f"ERROR: 'bounds' argument has keys {set(bounds.keys())}, but must have the keys {{'left', 'bottom', 'right', 'top'}}.")

        if crs is not None and not isinstance(crs, str):
            raise TypeError(f"ERROR: 'crs' argument is {type(crs)}, but it must be a string.")

        if driver is not None and not isinstance(driver, str):
            raise TypeError(f"ERROR: 'driver' argument is {type(driver)}, but it must be a string.")

        if no_data is not None and not isinstance(no_data, (int, float)):
            raise TypeError(f"ERROR: 'no_data' argument is {type(no_data)}, but it must be an integer or float.")

        if transform is not None and not (isinstance(transform, tuple) and len(transform) == 6 and
                                          all((isinstance(value, (int, float)) for value in transform))):
            raise TypeError(f"ERROR: 'transform' argument is {type(transform)}, but it must be a tuple of six floats.")

        if units is not None and not isinstance(units, str):
            raise TypeError(f"ERROR: 'units' argument is {type(units)}, but it must be a string.")

        self._array = array
        self._bounds = bounds
        self._crs = crs
        self._driver = driver
        self._no_data = no_data
        self._transform = transform
        self._units = units

    def __call__(self, new_array: Optional[np.ndarray[np.int32]] = None) -> (
            Optional)[np.ndarray[Union[np.uint8, np.int32]]]:
        if new_array is not None:
            self._array = new_array
        return self._array

    def __str__(self):
        return str({
            'crs': self.crs,
            'driver': self.driver,
            'bounds': self.bounds,
            'no_data': self.no_data,
            'transform': self.transform,
            'units': self.units,
            'width': self.width,
            'height': self.height,
            'count': self.count,
            'mean': self.mean,
            'median': self.median,
            'minimum': self.min,
            'maximum': self.max,
            'standard_deviation': self.std_dev,
        })

    @property
    def bounds(self) -> Optional[Dict[str, float]]:
        return self._bounds

    @property
    def crs(self) -> Optional[str]:
        return self._crs

    @property
    def driver(self) -> Optional[str]:
        return self._driver

    @property
    def no_data(self) -> Optional[Union[int, float]]:
        return self._no_data

    @property
    def transform(self) -> Optional[Tuple[float, float, float, float, float, float]]:
        return self._transform

    @property
    def units(self) -> Optional[str]:
        return self._units

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
    def mean(self) -> Optional[List[float]]:
        if self._array is not None:
            return np.mean(self._array) if len(self._array.shape) <= 2 else [np.mean(self._array[:, :, i]) for i in range(self._array.shape[2])]
        else:
            return None

    @property
    def median(self) -> Optional[List[float]]:
        if self._array is not None:
            return np.median(self._array) if len(self._array.shape) <= 2 else [np.median(self._array[:, :, i]) for i in range(self._array.shape[2])]
        else:
            return None

    @property
    def min(self) -> Optional[List[Union[int, float]]]:
        if self._array is not None:
            return np.min(self._array) if len(self._array.shape) <= 2 else [np.min(self._array[:, :, i]) for i in range(self._array.shape[2])]
        else:
            return None

    @property
    def max(self) -> Optional[List[Union[int, float]]]:
        if self._array is not None:
            return np.max(self._array) if len(self._array.shape) <= 2 else [np.max(self._array[:, :, i]) for i in range(self._array.shape[2])]
        else:
            return None

    @property
    def std_dev(self) -> Optional[List[float]]:
        if self._array is not None:
            return np.std(self._array) if len(self._array.shape) <= 2 else [np.std(self._array[:, :, i]) for i in range(self._array.shape[2])]
        else:
            return None