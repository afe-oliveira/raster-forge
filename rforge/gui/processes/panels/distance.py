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

        super()._scroll_content_callback()

    def _build_callback(self):
        input_layer = _data.raster.layers[self._references["Layer"].currentText()].array
        input_alpha = (
            _data.raster.layers[self._references["Alpha"].currentText()].array
            if self._references["Alpha"].currentText() != "None"
            else None
        )

        layer = Layer()
        layer.array = distance(layer=input_layer, alpha=input_alpha)
        _data.viewer = layer
        _data.viewer_changed.emit()

        super()._build_callback()
