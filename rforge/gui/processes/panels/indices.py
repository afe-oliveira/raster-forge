from typing import Type

import numpy as np
import spyndex
from PySide6.QtWidgets import QLabel

from rforge.containers.layer import Layer
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.data import _data
from rforge.gui.processes.process_panel import _ProcessPanel
from rforge.processes.composite import PRESET_COMPOSITES
from rforge.processes.index import index

ARRAY_TYPE: Type[np.ndarray] = np.ndarray


class _IndicesPanel(_ProcessPanel):
    def __init__(self, name=None, selector=False, parent=None):
        super().__init__(name=name, selector=selector, parent=parent)

        for key in spyndex.indices.keys():
            self.selector_combo.addItem(key)

        self._scroll_content_callback()

    def _scroll_content_callback(self):
        self._widgets = {}
        self._references["Bands"] = {}
        self._references["Constants"] = {}

        index = spyndex.indices[self.selector_combo.currentText()]
        inputs = index.bands

        for input in inputs:
            if input in spyndex.bands:
                band = spyndex.bands[input]
                widget, reference = _adaptative_input(band.long_name, ARRAY_TYPE)

                self._widgets[band] = widget
                self._references["Bands"][band] = reference
            elif input in spyndex.constants:
                constant = spyndex.bands[input]
                widget, reference = _adaptative_input(
                    constant.long_name, float, constant.default
                )

                self._widgets[constant] = widget
                self._references["Constants"][constant] = reference

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"] = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        # Add Threshold
        self._widgets["Thresholds"], self._references["Thresholds"] = _adaptative_input(
            "Thresholds", range
        )

        # Add Binarization
        self._widgets["Binarize"], self._references["Binarize"] = _adaptative_input(
            "Binarize", bool
        )

        super()._scroll_content_callback()

    def _build_callback(self):
        selected_index = self.selector_combo.currentText()
        parameters = {}

        # Get Bands
        for key, value in self._references["Bands"].items():
            parameters[key.short_name] = _data.raster.layers[value.currentText()].array

        # Get Constants
        for key, value in self._references["Constants"].items():
            parameters[key.short_name] = value.value()

        alpha = (
            _data.raster.layers[self._references["Alpha"].currentText()].array
            if self._references["Alpha"].currentText() != "None"
            else None
        )
        thresholds = self._references["Thresholds"].value()
        binarize = False

        layer = Layer()
        layer.array = index(selected_index, parameters, alpha, thresholds, binarize)
        _data.viewer = layer
        _data.viewer_changed.emit()

        super()._build_callback()
