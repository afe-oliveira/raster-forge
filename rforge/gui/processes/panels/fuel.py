from typing import Type

import numpy as np
from matplotlib.colors import Normalize

from rforge.containers.layer import Layer
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.data import _data
from rforge.gui.processes.process_panel import _ProcessPanel
from rforge.processes.composite import PRESET_COMPOSITES, composite
from rforge.processes.distance import distance
from rforge.processes.topography import aspect, slope

ARRAY_TYPE: Type[np.ndarray] = np.ndarray


class _FuelMapPanel(_ProcessPanel):
    def __init__(self, name=None, selector=False, parent=None):
        super().__init__(name=name, selector=selector, parent=parent)

        self._scroll_content_callback()

    def _scroll_content_callback(self):
        self._widgets = {}
        self._references = {}

        # Add Vegetation Coverage
        (
            self._widgets["Vegetation Coverage"],
            self._references["Vegetation Coverage"],
        ) = _adaptative_input("Vegetation Coverage", ARRAY_TYPE)

        # Add Canopy Height
        self._widgets["Canopy Height"], self._references["Canopy Height"] = (
            _adaptative_input("Canopy Height", ARRAY_TYPE)
        )

        # Add Distance Field
        self._widgets["Distance Field"], self._references["Distance Field"] = (
            _adaptative_input("Distance Field", ARRAY_TYPE)
        )

        # Add Water Features
        self._widgets["Water Features"], self._references["Water Features"] = (
            _adaptative_input("Water Features", ARRAY_TYPE)
        )

        # Add Artificial Structures
        (
            self._widgets["Artificial Structures"],
            self._references["Artificial Structures"],
        ) = _adaptative_input("Artificial Structures", ARRAY_TYPE)

        # Add Fuel Models
        self._widgets["Fuel F"], self._references["Fuel F"] = _adaptative_input(
            "Fuel Model (Trees)", int, 200
        )
        self._widgets["Fuel V"], self._references["FuelV"] = _adaptative_input(
            "Fuel Model (Vegetation)", int, 200
        )
        self._widgets["Fuel M"], self._references["Fuel M"] = _adaptative_input(
            "Fuel Model (Mixed)", int, 200
        )

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"] = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        super()._scroll_content_callback()

    def _build_callback(self):
        super()._build_callback()
