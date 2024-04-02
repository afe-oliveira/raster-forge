from typing import Type

import numpy as np
from rforge.lib.containers.layer import Layer
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.data import _data
from rforge.gui.processes.process_panel import _ProcessPanel
from rforge.lib.processes.height import height

ARRAY_TYPE: Type[np.ndarray] = np.ndarray


class _HeightPanel(_ProcessPanel):
    def __init__(self, name=None, selector=False, parent=None):
        super().__init__(name=name, selector=selector, parent=parent)

        self._scroll_content_callback()

    def _scroll_content_callback(self):
        self._widgets = {}
        self._references = {}

        # Add DTM
        self._widgets["DTM"], self._references["DTM"], _ = _adaptative_input(
            "DTM", ARRAY_TYPE
        )

        # Add DSM
        self._widgets["DSM"], self._references["DSM"], _ = _adaptative_input(
            "DSM", ARRAY_TYPE
        )

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"], _ = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        super()._scroll_content_callback()

    def _build_callback(self):
        input_dtm = _data.raster.layers[self._references["DTM"].currentText()].array
        input_dsm = _data.raster.layers[self._references["DSM"].currentText()].array
        input_alpha = (
            _data.raster.layers[self._references["Alpha"].currentText()].array
            if self._references["Alpha"].currentText() != "None"
            else None
        )

        layer = height(dtm=input_dtm, dsm=input_dsm, alpha=input_alpha)
        _data.viewer = layer
        _data.viewer_changed.emit()

        super()._build_callback()
