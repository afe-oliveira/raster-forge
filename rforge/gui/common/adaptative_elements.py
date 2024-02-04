from typing import Any, Type

import numpy as np
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from superqt import QLabeledDoubleRangeSlider

from rforge.gui.data import _data


def _adaptative_label(data, label, sub_labels=None):
    widget = QWidget()
    layout = QVBoxLayout()

    item_layout = QHBoxLayout()

    base_label = QLabel(label)
    base_label.setObjectName("simple-label") if not isinstance(data, (tuple, list, dict)) else base_label.setObjectName("title-label")
    base_label.setContentsMargins(5, 5, 5, 5)

    item_layout.addWidget(base_label)
    item_layout.addStretch(100)

    if data is None or isinstance(data, (str, int, float)):
        if data is None:
            value_label = QLabel("N/A")
        else:
            value_label = str(round(data, 4)) if isinstance(data, float) else str(data)

        item_layout.addWidget(QLabel(value_label))
        layout.addLayout(item_layout)
    else:
        # Add Base Label
        layout.addLayout(item_layout)

        items = []
        if isinstance(data, (tuple, list)):
            for i, item in enumerate(data):
                items.append((f"{sub_labels[i] if sub_labels else f'Item {i + 1}'}", item))
        elif isinstance(data, dict):
            for key, value in data.items():
                items.append((f"{sub_labels[key] if sub_labels else key}", value))

        for item in items:
            layout.addWidget(_adaptative_label(item[1], item[0]))

    widget.setLayout(layout)
    return widget


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
