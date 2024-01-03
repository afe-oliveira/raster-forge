import inspect

import numpy as np
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea, QProgressBar, QComboBox, QLineEdit, \
    QLabel, QGroupBox, QGridLayout

from ProjectNabu.container.layer import Layer

from ProjectNabu.gui.data import data

class AdaptativePanel(QWidget):
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

        # Add ComboBox and Scroll Area to the main layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.indices_combo)
        layout.addWidget(self.scroll_area)

        # Create a QGridLayout for the buttons
        buttons_layout = QGridLayout()

        # Add Back Button
        back_button = QPushButton('Back', self)
        back_button.clicked.connect(self.back_clicked)
        buttons_layout.addWidget(back_button, 0, 0, 1, 1)

        # Add Progress Bar
        progress_bar = QProgressBar(self)
        buttons_layout.addWidget(progress_bar, 0, 1, 1, 23)

        # Add Build Button
        build_button = QPushButton('Build', self)
        build_button.clicked.connect(self.build_clicked)
        buttons_layout.addWidget(build_button, 0, 24, 1, 1)

        # Add the buttons layout to the main layout
        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.indices_combo.currentIndexChanged.connect(self.update_scroll_content)
        self.update_scroll_content(0)

    def update_scroll_content(self, index):
        # Clear Existing Widgets
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.takeAt(i).widget()
            if widget:
                widget.deleteLater()

        selected_function = list(self.plugins.values())[index]

        parameters = inspect.signature(selected_function).parameters

        self.input_values = {}
        for param_name, param in parameters.items():
            label = QLabel(f"{param_name.upper()}", self)

            if param.annotation == np.ndarray:
                widget = QComboBox(self)
                if data.raster is not None:
                    keys_from_raster = list(data.raster.layers.keys())
                    widget.addItems(keys_from_raster)
            elif getattr(param.annotation, '__origin__', None) == tuple:
                tuple_types = getattr(param.annotation, '__args__', ())
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

    def back_clicked(self):
        data.process_main.emit()

    def build_clicked(self):
        # Get the Selected Plugin Function
        function = list(self.plugins.values())[self.indices_combo.currentIndex()]

        parameters = inspect.signature(function).parameters
        input_values = []

        for param_name, param in parameters.items():
            widget = self.input_values.get(param_name)

            if param.annotation == np.ndarray:
                if isinstance(widget, QComboBox) and data.raster is not None:
                    selected_layer = widget.currentText()
                    input_values.append(data.raster.layers[selected_layer].data)
            elif getattr(param.annotation, '__origin__', None) == tuple:
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

        layer = Layer()
        layer.data = function(*input_values)
        data.viewer = layer
        data.viewer_changed.emit()