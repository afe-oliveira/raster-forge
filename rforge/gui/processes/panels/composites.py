from typing import Type

import numpy as np
from rforge.gui.common.adaptative_elements import _adaptative_input
from rforge.gui.data import _data
from rforge.gui.processes.process_panel import _ProcessPanel
from rforge.library.processes.composite import PRESET_COMPOSITES, composite

ARRAY_TYPE: Type[np.ndarray] = np.ndarray


class _CompositesPanel(_ProcessPanel):
    def __init__(self, name=None, selector=False, parent=None):
        super().__init__(name=name, selector=selector, parent=parent)

        for key in PRESET_COMPOSITES.keys():
            self.selector_combo.addItem(key)

        self._scroll_content_callback()

    def _scroll_content_callback(self):
        self._widgets = {}
        self._references = {}
        for component in PRESET_COMPOSITES[self.selector_combo.currentText()]:
            widget, reference, _ = _adaptative_input(component, ARRAY_TYPE)

            self._widgets[component] = widget
            self._references[component] = reference

        # Add Alpha
        self._widgets["Alpha"], self._references["Alpha"], _ = _adaptative_input(
            "Alpha", ARRAY_TYPE, "None"
        )

        # Add Gammas
        for component in PRESET_COMPOSITES[self.selector_combo.currentText()]:
            (
                self._widgets[f"Gamma {component}"],
                self._references[f"Gamma {component}"],
                _,
            ) = _adaptative_input(f"Gamma {component}", float, 1)

        super()._scroll_content_callback()

    def _build_callback(self):
        input_layers = []
        for component in PRESET_COMPOSITES[self.selector_combo.currentText()]:
            input_layers.append(
                _data.raster.layers[self._references[component].currentText()].array
            )

        input_alpha = (
            _data.raster.layers[self._references["Alpha"].currentText()].array
            if self._references["Alpha"].currentText() != "None"
            else None
        )

        input_gamma = []
        for component in PRESET_COMPOSITES[self.selector_combo.currentText()]:
            input_gamma.append(self._references[f"Gamma {component}"].value())

        layer = composite(layers=input_layers, alpha=input_alpha, gamma=input_gamma)

        _data.viewer = layer
        _data.viewer_changed.emit()

        super()._build_callback()
