from typing import Type

import numpy as np
from PySide6.QtCore import Qt
from matplotlib.colors import Normalize

from rforge.containers.layer import Layer
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.data import _data
from rforge.gui.processes.process_panel import _ProcessPanel
from rforge.processes.composite import PRESET_COMPOSITES, composite
from rforge.processes.distance import distance
from rforge.processes.topography import aspect, slope

ARRAY_TYPE: Type[np.ndarray] = np.ndarray


class _DistanceFieldPanel(_ProcessPanel):
    def __init__(self, name=None, selector=False, parent=None):
        super().__init__(name=name, selector=selector, parent=parent)

        self._scroll_content_callback()

    def _scroll_content_callback(self):
        self._widgets = {}
        self._references = {}

        # Add Layer
        self._widgets["Layer"], self._references["Layer"], _ = _adaptative_input(
            "Layer", ARRAY_TYPE
        )
        self._references["Layer"].currentIndexChanged.connect(self._threshold_callback)

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"], _ = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        # Add Binarization
        self._widgets["Binarize"], self._references["Binarize"], self._references[
            "Binarize Toggle"] = _adaptative_input(
            "Binarize", range, None, True
        )

        # Add Mask Size
        self._widgets["Mask Size"], self._references["Mask Size"], _ = _adaptative_input(
            "Mask Size", list, ['3', '5']
        )

        # Add Inversion
        self._widgets["Inversion"], self._references["Inversion"], _ = _adaptative_input(
            "Invert", bool
        )

        self._references["Binarize Toggle"].stateChanged.connect(self._binarize_callback)
        self._binarize_callback()
        self._threshold_callback()

        super()._scroll_content_callback()


    def _build_callback(self):
        input_layer = _data.raster.layers[self._references["Layer"].currentText()].array
        input_alpha = (
            _data.raster.layers[self._references["Alpha"].currentText()].array
            if self._references["Alpha"].currentText() != "None"
            else None
        )
        input_thresholds = self._references["Binarize"].value() if self._references[
            "Binarize Toggle"].isChecked() else None
        input_mask_size = int(self._references["Mask Size"].currentText())
        input_invert = self._references["Inversion"].isChecked()

        layer = Layer()
        layer.array = distance(layer=input_layer, alpha=input_alpha, thresholds=input_thresholds, mask_size=input_mask_size, invert=input_invert)
        _data.viewer = layer
        _data.viewer_changed.emit()

        super()._build_callback()

    def _binarize_callback(self):
        self._references["Binarize"].setEnabled(self._references["Binarize Toggle"].isChecked())

    def _threshold_callback(self):
        if self._references["Layer"].currentText():
            input_layer = _data.raster.layers[self._references["Layer"].currentText()]
            self._references["Binarize"].setRange(input_layer.min, input_layer.max)
            self._references["Binarize"].setValue((input_layer.min, input_layer.max))