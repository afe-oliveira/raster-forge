from typing import Type

import numpy as np
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QGridLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from RasterForge.containers.layer import Layer
from RasterForge.gui.data import _data
from RasterForge.gui.common.adaptative_elements import adaptative_input
from RasterForge.processes.topographic import aspect, slope


class TopographicalPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a Combo Box for Available Topographical Processes
        self.topographic_combo = QComboBox(self)
        self.topographic_combo.addItem("Slope")
        self.topographic_combo.addItem("Aspect")

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
        layout.addWidget(self.topographic_combo)
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
        self.topographic_combo.currentIndexChanged.connect(self.update_scroll_content)

        # When Raster Data Changes, Update Inner Scroll Content
        _data.raster_changed.connect(self.update_scroll_content)

        # Start Scroll at First Position
        self.update_scroll_content(0)

    def update_scroll_content(self, index=0):
        # Clear Existing Widgets
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.takeAt(i).widget()
            if widget:
                widget.deleteLater()

        array_type: Type[np.ndarray] = np.ndarray
        self.inputs = {}

        # Add DEM Selection
        label = QLabel(f"Digital Elevation Model", self)
        widget = adaptative_input("Digital Elevation Model", array_type)
        self.scroll_layout.addWidget(label)
        self.scroll_layout.addWidget(widget)
        self.inputs["DEM"] = widget

        # Add Unit Selection
        label = QLabel(f"Units", self)
        widget = QComboBox(self)
        widget.addItem("Degrees")
        widget.addItem("Radians")
        self.scroll_layout.addWidget(label)
        self.scroll_layout.addWidget(widget)
        self.inputs["Units"] = widget

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
        self.inputs["Alpha"] = widget

    def back_clicked(self):
        _data.process_main.emit()

    def build_clicked(self):
        layer = Layer()
        if self.topographic_combo.currentText() == "Slope":
            layer.array = slope(
                dem=_data.raster.layers[self.inputs["DEM"].currentText()].array,
                units=self.inputs["Units"].currentText().lower(),
            )
        elif self.topographic_combo.currentText() == "Aspect":
            layer.array = aspect(
                dem=_data.raster.layers[self.inputs["DEM"].currentText()].array,
                units=self.inputs["Units"].currentText().lower(),
            )
        _data.viewer = layer
        _data.viewer_changed.emit()
