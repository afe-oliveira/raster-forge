from typing import Type

import numpy as np
from rforge.containers.layer import Layer
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.data import _data
from rforge.gui.processes.process_panel import _ProcessPanel
from rforge.processes.distance import distance

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

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"], _ = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        # Add Mask Size
        self._widgets["Mask Size"], self._references["Mask Size"], _ = (
            _adaptative_input("Mask Size", list, ["3", "5"])
        )

        # Add Binarization
        self._widgets["Binarization"], self._references["Binarization"], _ = (
            _adaptative_input("Binarize", bool)
        )
        self._widgets["Threshold Min"], self._references["Threshold Min"], _ = (
            _adaptative_input("Threshold Minimum", float)
        )
        self._widgets["Threshold Max"], self._references["Threshold Max"], _ = (
            _adaptative_input("Threshold Maximum", float)
        )

        # Add Inversion
        self._widgets["Inversion"], self._references["Inversion"], _ = (
            _adaptative_input("Invert", bool)
        )

        self._threshold_callback()
        self._binarize_callback()

        self._references["Layer"].currentIndexChanged.connect(self._threshold_callback)
        self._references["Binarization"].stateChanged.connect(self._binarize_callback)
        super()._scroll_content_callback()

    def _build_callback(self):
        input_layer = _data.raster.layers[self._references["Layer"].currentText()].array
        input_alpha = (
            _data.raster.layers[self._references["Alpha"].currentText()].array
            if self._references["Alpha"].currentText() != "None"
            else None
        )
        input_thresholds = (
            (
                self._references["Threshold Min"].value(),
                self._references["Threshold Max"].value(),
            )
            if self._references["Binarization"].isChecked()
            else None
        )
        input_mask_size = int(self._references["Mask Size"].currentText())
        input_invert = self._references["Inversion"].isChecked()

        layer = distance(
            layer=input_layer,
            alpha=input_alpha,
            thresholds=input_thresholds,
            mask_size=input_mask_size,
            invert=input_invert,
        )
        _data.viewer = layer
        _data.viewer_changed.emit()

        super()._build_callback()

    def _binarize_callback(self):
        self._references["Threshold Min"].setEnabled(
            self._references["Binarization"].isChecked()
        )
        self._references["Threshold Max"].setEnabled(
            self._references["Binarization"].isChecked()
        )

    def _threshold_callback(self):
        if self._references["Layer"].currentText():
            input_layer = _data.raster.layers[self._references["Layer"].currentText()]

            self._references["Threshold Min"].setRange(input_layer.min, input_layer.max)
            self._references["Threshold Min"].setValue(input_layer.min)

            self._references["Threshold Max"].setRange(input_layer.min, input_layer.max)
            self._references["Threshold Max"].setValue(input_layer.max)
        else:
            self._references["Threshold Min"].setRange(0, 0)
            self._references["Threshold Min"].setValue(0)

            self._references["Threshold Max"].setRange(0, 0)
            self._references["Threshold Max"].setValue(0)
