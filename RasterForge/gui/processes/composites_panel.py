import inspect
from typing import Type

import numpy as np
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QScrollArea,
    QProgressBar,
    QComboBox,
    QLineEdit,
    QLabel,
    QGroupBox,
    QGridLayout,
    QFrame,
    QDoubleSpinBox,
)

from RasterForge.containers.layer import Layer

from RasterForge.gui.data import data
from RasterForge.gui.processes.adaptative_elements import adaptative_input

from RasterForge.processes.composite import PRESET_COMPOSITES, composite


class CompositesPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a Combo Box for Available Presets
        self.composites_combo = QComboBox(self)
        self.composites_combo.addItem("Custom")
        for key in PRESET_COMPOSITES.keys():
            self.composites_combo.addItem(key)

        # Create a Scroll Area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget(self)
        self.scroll_area.setWidget(self.scroll_content)

        # Create a Vertical Layout for the Scroll Content (Aligned Top)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        # Add the Combo Box and Scroll Area to the main layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.composites_combo)
        layout.addWidget(self.scroll_area)

        # Create a Grid Layout for the General UI
        buttons_layout = QGridLayout()

        # Add Back Button
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(self.back_clicked)
        buttons_layout.addWidget(back_button, 0, 0, 1, 1)

        # Add Progress Bar
        progress_bar = QProgressBar(self)
        buttons_layout.addWidget(progress_bar, 0, 1, 1, 23)

        # Add Build Button
        build_button = QPushButton("Build", self)
        build_button.clicked.connect(self.build_clicked)
        buttons_layout.addWidget(build_button, 0, 24, 1, 1)

        # Add the Buttons Layout to the Main Layout
        layout.addLayout(buttons_layout)

        # Set Layout
        self.setLayout(layout)

        # When Combo Box Selection Changes, Update Inner Scroll Content
        self.composites_combo.currentIndexChanged.connect(self.update_scroll_content)

        # When Raster Data Changes, Update Inner Scroll Content
        data.raster_changed.connect(self.update_scroll_content)

        # Start Scroll at First Position
        self.update_scroll_content(0)

    def update_scroll_content(self, index=0):
        # Clear Existing Widgets
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.takeAt(i).widget()
            if widget:
                widget.deleteLater()

        selection = self.composites_combo.currentText()
        array_type: Type[np.ndarray] = np.ndarray

        self.input_layers = {}
        if selection == "Custom":
            pass
        else:
            composite_components = PRESET_COMPOSITES[selection]
            for component in composite_components:
                label = QLabel(f"{component}", self)
                widget = adaptative_input(component, array_type)

                self.scroll_layout.addWidget(label)
                self.scroll_layout.addWidget(widget)

                self.input_layers[component] = widget

        # Add Separator
        separator_line = QFrame(self)
        separator_line.setFrameShape(QFrame.HLine)
        separator_line.setFrameShadow(QFrame.Sunken)
        self.scroll_layout.addWidget(separator_line)

        # Add Alpha Selection
        label = QLabel(f"Alpha", self)
        widget = adaptative_input("Alpha", array_type)
        self.scroll_layout.addWidget(label)
        self.scroll_layout.addWidget(widget)

        # Add Separator
        self.scroll_layout.addWidget(separator_line)

        # Gamma Selection
        self.input_gamma = {}
        for key in self.input_layers.keys():
            float_label = QLabel(f"{key} Gamma", self)
            float_spinbox = QDoubleSpinBox(self)
            float_spinbox.setDecimals(2)

            self.scroll_layout.addWidget(float_label)
            self.scroll_layout.addWidget(float_spinbox)

            self.input_gamma[key] = float_spinbox

    def back_clicked(self):
        data.process_main.emit()

    def build_clicked(self):
        input_layers = []
        for key, value in self.input_layers.items():
            input_layers.append(data.raster.layers[value.currentText()].array)

        input_alpha = None

        input_gamma = []
        for key, value in self.input_gamma.items():
            input_gamma.append(value.value())

        layer = Layer()
        layer.array = composite(
            layers=input_layers, alpha=input_alpha, gamma=input_gamma
        )
        data.viewer = layer
        data.viewer_changed.emit()
