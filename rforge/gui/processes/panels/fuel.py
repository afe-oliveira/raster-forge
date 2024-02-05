from typing import Type

import numpy as np
from rforge.containers.layer import Layer
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.data import _data
from rforge.gui.processes.process_panel import _ProcessPanel
from rforge.processes.fuel import fuel

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

        # Add Tree Height
        self._widgets["Tree Height"], self._references["Tree Height"], _ = (
            _adaptative_input("Tree Height", float, 1)
        )

        # Add Fuel Models
        self._widgets["Fuel F"], self._references["Fuel F"], _ = _adaptative_input(
            "Fuel Model (Trees)", int, 210
        )
        self._widgets["Fuel V"], self._references["Fuel V"], _ = _adaptative_input(
            "Fuel Model (Vegetation)", int, 230
        )
        self._widgets["Fuel M"], self._references["Fuel M"], _ = _adaptative_input(
            "Fuel Model (Mixed)", int, 220
        )

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"], _ = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        super()._scroll_content_callback()

    def _build_callback(self):
        input_coverage = _data.raster.layers[
            self._references["Vegetation Coverage"].currentText()
        ].array
        input_height = _data.raster.layers[
            self._references["Canopy Height"].currentText()
        ].array
        input_distance = _data.raster.layers[
            self._references["Distance Field"].currentText()
        ].array
        input_water = _data.raster.layers[
            self._references["Water Features"].currentText()
        ].array
        input_artificial = _data.raster.layers[
            self._references["Artificial Structures"].currentText()
        ].array

        input_alpha = (
            _data.raster.layers[self._references["Alpha"].currentText()].array
            if self._references["Alpha"].currentText() != "None"
            else None
        )

        input_models = (
            self._references["Fuel F"].value(),
            self._references["Fuel M"].value(),
            self._references["Fuel V"].value(),
        )
        input_tree_height = self._references["Tree Height"].value()

        layer = Layer()
        layer.array = fuel(
            coverage=input_coverage,
            distance=input_distance,
            height=input_height,
            water=input_water,
            artificial=input_artificial,
            alpha=input_alpha,
            tree_height=input_tree_height,
            models=input_models,
        )
        _data.viewer = layer
        _data.viewer_changed.emit()
        super()._build_callback()
