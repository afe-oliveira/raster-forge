from typing import Union, Dict, Optional, Tuple

import numpy as np


class Layer:
    _data: Optional[np.ndarray[Union[np.uint8, np.int32]]] = None
    _metadata: Optional[Dict[str, Union[str, int, float]]] = None
    _projection: Optional[str] = None
    _transform: Optional[Tuple[float, float, float, float, float, float]] = None

    def __init__(
        self,
        data: Optional[np.ndarray[Union[np.uint8, np.int32]]] = None,
        metadata: Optional[Dict[str, Union[str, int, float]]] = None,
        projection: Optional[str] = None,
        transform: Optional[Tuple[float, float, float, float, float, float]] = None,
    ):
        self._data = data
        self._metadata = metadata
        self._projection = projection
        self._transform = transform

    @property
    def data(self) -> Optional[np.ndarray[Union[np.uint8, np.int32]]]:
        return self._data

    @data.setter
    def data(self, value: Optional[np.ndarray[Union[np.uint8, np.int32]]]):
        self._data = value

    @property
    def metadata(self) -> Optional[Dict[str, Union[str, int, float]]]:
        return self._metadata

    @metadata.setter
    def metadata(self, value: Optional[Dict[str, Union[str, int, float]]]):
        self._metadata = value

    @property
    def projection(self) -> Optional[str]:
        return self._projection

    @projection.setter
    def projection(self, value: Optional[str]):
        self._projection = value

    @property
    def transform(self) -> Optional[Tuple[float, float, float, float, float, float]]:
        return self._transform

    @transform.setter
    def transform(self, value: Optional[Tuple[float, float, float, float, float, float]]):
        self._transform = value
