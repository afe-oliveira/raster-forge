import inspect
from typing import get_args

import numpy as np
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from RasterForge.containers.layer import Layer
from RasterForge.gui.data import _data
from RasterForge.processes.index import index


class IndicesPanel(QWidget):
    def __init__(self, plugins, parent=None):
        super().__init__(parent)
        self.plugins = plugins

        # Create a Combo Box for Available Plugins
        self.indices_combo = QComboBox(self)

        # Add Available Plugins
        for name, function in self.plugins.items():
            self.indices_combo.addItem(str(name).upper())

        # Create a Scroll Area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget(self)
        self.scroll_area.setWidget(self.scroll_content)

        # Create a layout for the scroll content
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        # Add ComboBox and Scroll Area to the main layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.indices_combo)
        layout.addWidget(self.scroll_area)

        # Create a QGridLayout for the buttons
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

        # Add the buttons layout to the main layout
        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.indices_combo.currentIndexChanged.connect(self.update_scroll_content)
        _data.raster_changed.connect(self.update_scroll_content)
        self.update_scroll_content(0)

    def update_scroll_content(self, index=0):
        # Clear Existing Widgets
        for i in reversed(range(self.scroll_layout.count())):
            item = self.scroll_layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    sublayout = item.layout()
                    while sublayout.count() > 0:
                        subwidget = sublayout.takeAt(0).widget()
                        if subwidget:
                            subwidget.deleteLater()

        selected_function = list(self.plugins.values())[index]

        parameter_names = list(inspect.signature(selected_function()).parameters.keys())
        parameter_types = [
            arg
            for return_type in get_args(
                inspect.signature(selected_function).return_annotation
            )[:-1]
            for arg in (
                return_type if isinstance(return_type, tuple) else [return_type]
            )
            if arg is not inspect.Signature.empty
        ][0]

        self.input_values = {}
        for param_name, param_type in zip(parameter_names, parameter_types):
            label = QLabel(f"{param_name.upper()}", self)

            if param_type == np.ndarray:
                widget = QComboBox(self)
                if _data.raster is not None:
                    keys_from_raster = list(_data.raster.layers.keys())
                    widget.addItems(keys_from_raster)
            elif getattr(param_type, "__origin__", None) == tuple:
                tuple_types = getattr(param_type, "__args__", ())
                widget_group = QGroupBox(self)
                group_layout = QVBoxLayout()
                for i, subtype in enumerate(tuple_types):
                    sub_label = QLabel(f"{param_name.upper()}[{i}]", self)
                    sub_widget = QLineEdit(self)
                    sub_widget.setObjectName(f"{param_name.upper()}_{i}")
                    group_layout.addWidget(sub_label)
                    group_layout.addWidget(sub_widget)
                widget_group.setLayout(group_layout)
                widget = widget_group
            else:
                widget = QLineEdit(self)
                widget.setObjectName(f"{param_name.upper()}")

            self.scroll_layout.addWidget(label)
            self.scroll_layout.addWidget(widget)

            self.input_values[param_name] = widget

        # Add Separator
        separator = QFrame(self)
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.scroll_layout.addWidget(separator)

        # Add ALPHA parameter
        alpha_label = QLabel("ALPHA", self)
        alpha_widget = QComboBox(self)
        alpha_widget.addItem("None")
        if _data.raster is not None:
            keys_from_raster = list(_data.raster.layers.keys())
            alpha_widget.addItems(keys_from_raster)
        alpha_widget.setObjectName("ALPHA")

        self.scroll_layout.addWidget(alpha_label)
        self.scroll_layout.addWidget(alpha_widget)

        self.input_values["ALPHA"] = alpha_widget

        # Add Range Selector
        alpha_range_label = QLabel("RANGE", self)
        alpha_range_layout = QHBoxLayout()

        alpha_min_label = QLabel("Min:", self)
        alpha_min_spinbox = QDoubleSpinBox(self)
        alpha_min_spinbox.setRange(-1, 1)
        alpha_min_spinbox.setSingleStep(0.05)
        alpha_min_spinbox.setValue(-1)

        alpha_max_label = QLabel("Max:", self)
        alpha_max_spinbox = QDoubleSpinBox(self)
        alpha_max_spinbox.setRange(-1, 1)
        alpha_max_spinbox.setSingleStep(0.05)
        alpha_max_spinbox.setValue(1)

        alpha_range_layout.addWidget(alpha_min_label)
        alpha_range_layout.addWidget(alpha_min_spinbox)
        alpha_range_layout.addWidget(alpha_max_label)
        alpha_range_layout.addWidget(alpha_max_spinbox)

        self.scroll_layout.addWidget(alpha_range_label)
        self.scroll_layout.addLayout(alpha_range_layout)

        self.input_values["RANGE"] = (alpha_min_spinbox, alpha_max_spinbox)

    def back_clicked(self):
        _data.process_main.emit()

    def build_clicked(self):
        # Get the Selected Plugin Function
        function = list(self.plugins.values())[self.indices_combo.currentIndex()]

        input_values = []

        parameter_names = list(inspect.signature(function()).parameters.keys())
        parameter_types = [
            arg
            for return_type in get_args(inspect.signature(function).return_annotation)[
                :-1
            ]
            for arg in (
                return_type if isinstance(return_type, tuple) else [return_type]
            )
            if arg is not inspect.Signature.empty
        ][0]

        for param_name, param_type in zip(parameter_names, parameter_types):
            if param_name != "ALPHA":
                widget = self.input_values.get(param_name)

                if param_type == np.ndarray:
                    if isinstance(widget, QComboBox) and _data.raster is not None:
                        selected_layer = widget.currentText()
                        input_values.append(_data.raster.layers[selected_layer].array)
                elif getattr(param_type, "__origin__", None) == tuple:
                    tuple_values = []
                    if isinstance(widget, QGroupBox):
                        for i in range(widget.layout().count()):
                            sub_widget = widget.layout().itemAt(i).widget()
                            if isinstance(sub_widget, QLineEdit):
                                tuple_values.append(float(sub_widget.text()))
                        input_values.append(tuple(tuple_values))
                else:
                    if isinstance(widget, QLineEdit):
                        input_values.append(float(widget.text()))

        alpha_value = self.input_values.get("ALPHA").currentText()
        alpha_value = (
            None if alpha_value == "None" else _data.raster.layers[alpha_value].array
        )

        min_spinbox, max_spinbox = self.input_values["RANGE"]

        layer = Layer()
        layer.data = index(
            function(),
            alpha_value,
            (min_spinbox.value(), max_spinbox.value()),
            *input_values,
        )

        _data.viewer = layer
        _data.viewer_changed.emit()
