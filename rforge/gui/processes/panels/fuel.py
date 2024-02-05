from typing import Type

import numpy as np
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.processes.process_panel import _ProcessPanel

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
            _,
        ) = _adaptative_input("Vegetation Coverage", ARRAY_TYPE)

        # Add Canopy Height
        self._widgets["Canopy Height"], self._references["Canopy Height"], _ = (
            _adaptative_input("Canopy Height", ARRAY_TYPE)
        )

        # Add Distance Field
        self._widgets["Distance Field"], self._references["Distance Field"], _ = (
            _adaptative_input("Distance Field", ARRAY_TYPE)
        )

        # Add Water Features
        self._widgets["Water Features"], self._references["Water Features"], _ = (
            _adaptative_input("Water Features", ARRAY_TYPE)
        )

        # Add Artificial Structures
        (
            self._widgets["Artificial Structures"],
            self._references["Artificial Structures"],
            _,
        ) = _adaptative_input("Artificial Structures", ARRAY_TYPE)

        # Add Fuel Models
        self._widgets["Fuel F"], self._references["Fuel F"], _ = _adaptative_input(
            "Fuel Model (Trees)", int, 200
        )
        self._widgets["Fuel V"], self._references["FuelV"], _ = _adaptative_input(
            "Fuel Model (Vegetation)", int, 200
        )
        self._widgets["Fuel M"], self._references["Fuel M"], _ = _adaptative_input(
            "Fuel Model (Mixed)", int, 200
        )

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"], _ = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        super()._scroll_content_callback()

    def _build_callback(self):
        super()._build_callback()
