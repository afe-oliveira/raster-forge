from typing import Any, Type

import numpy as np
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from superqt import QLabeledDoubleRangeSlider

from rforge.gui.data import _data


def adaptative_label(data, label, sub_labels=None):
    widgets = []

    base_label = QLabel(label)
    base_label.setObjectName("simple-label")
    base_label.setFixedWidth(125)
    base_label.setContentsMargins(5, 5, 5, 5)

    if data is None:
        widget = QWidget()

        # Create Label for Data
        value_label = QLabel("N/A")
        value_label.setObjectName("simple-label-no-bg")

        # Create Horizontal Layout for Row
        layout = QHBoxLayout()

        # Add Labels to Row
        layout.addWidget(base_label)
        layout.addWidget(value_label)

        # Set the layout for the widget
        widget.setLayout(layout)

        widgets.append(widget)
    elif isinstance(data, (str, int, float)):
        widget = QWidget()

        # Create Label for Data
        label_text = str(round(data, 4)) if isinstance(data, float) else str(data)
        value_label = QLabel(label_text)
        value_label.setObjectName("simple-label-no-bg")

        # Create Horizontal Layout for Row
        layout = QHBoxLayout()

        # Add Labels to Row
        layout.addWidget(base_label)
        layout.addWidget(value_label)

        # Set the layout for the widget
        widget.setLayout(layout)

        widgets.append(widget)
    else:
        # Add Base Label
        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(base_label)
        widgets.append(widget)

        # Add Inner Elements
        if isinstance(data, tuple):
            for i, item in enumerate(data):
                # Create Label for Data
                label_text = f"{sub_labels[i] if sub_labels else f'Item {i + 1}'}"

                # Recursive Function
                inner_widgets = adaptative_label(item, label_text)

                # Append Inner Widgets to the Existing Widgets List
                widgets.extend(inner_widgets)
        elif isinstance(data, dict):
            for key, value in data.items():
                # Create Label for Data
                label_text = f"{sub_labels[key] if sub_labels else key}"

                # Recursive Function
                inner_widgets = adaptative_label(value, label_text)

                # Append Inner Widgets to the Existing Widgets List
                widgets.extend(inner_widgets)

    return widgets


def _adaptative_input(
    name: str, type: Type, preset: Any = None, optional: bool = False
):
    widget = QWidget()
    value_ref = None
    optional_ref = None

    layout = QVBoxLayout()
    label_layout = QHBoxLayout()

    label = QLabel(f"{name}")
    label.setObjectName("simple-label")
    label.setMinimumHeight(25)
    label.setMaximumHeight(25)

    label_layout.addWidget(label)
    label_layout.addStretch(100)

    if optional or type == bool:
        optional_ref = QCheckBox()
        label_layout.addWidget(optional_ref)

    layout.addLayout(label_layout)

    if type == bool:
        widget.setLayout(layout)
        return widget, optional_ref, None
    elif type == np.ndarray:
        combo_box = QComboBox()
        if preset is not None:
            combo_box.addItem(preset)
        if _data.raster is not None:
            keys_from_raster = list(_data.raster.layers.keys())
            combo_box.addItems(keys_from_raster)

        value_ref = combo_box

        layout.addWidget(combo_box)
        widget.setLayout(layout)
    elif type in [int, float]:
        spin_box = QSpinBox() if type == int else QDoubleSpinBox()
        spin_box.setObjectName("spin-box")
        spin_box.setRange(0, 9999)
        spin_box.setSingleStep(1) if type == int else spin_box.setSingleStep(0.1)
        spin_box.setValue(preset) if preset is not None else 0

        value_ref = spin_box

        layout.addWidget(spin_box)
        widget.setLayout(layout)
    elif type == range:
        range_slider = QLabeledDoubleRangeSlider(Qt.Orientation.Horizontal)
        if preset is None:
            preset = (-1, 1)
        range_slider.setRange(preset[0], preset[1])
        range_slider.setValue(preset)

        value_ref = range_slider

        layout.addWidget(range_slider)
        widget.setLayout(layout)
    elif type == list:
        combo_box = QComboBox()
        if preset:
            for item in preset:
                combo_box.addItem(item)

        value_ref = combo_box

        layout.addWidget(combo_box)
        widget.setLayout(layout)

    return widget, value_ref, optional_ref
