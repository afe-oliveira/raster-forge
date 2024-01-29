from typing import Any, Type

import numpy as np
from PySide6.QtWidgets import QComboBox, QGroupBox, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout

from RasterForge.gui.data import _data


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


def adaptative_input(name: str, type: Type):
    widget = None

    # Data Type is an Numpy Array
    if type == np.ndarray:
        widget = QComboBox()
        if _data.raster is not None:
            keys_from_raster = list(_data.raster.layers.keys())
            widget.addItems(keys_from_raster)
    # Data Type is a Tuple
    elif getattr(type, "__origin__", None) == tuple:
        tuple_types = getattr(type, "__args__", ())
        widget_group = QGroupBox()
        group_layout = QVBoxLayout()
        for i, subtype in enumerate(tuple_types):
            sub_label = QLabel(f"{name}[{i}]")
            sub_widget = QLineEdit()
            sub_widget.setText("1")
            sub_widget.setObjectName(f"{name}_{i}")
            group_layout.addWidget(sub_label)
            group_layout.addWidget(sub_widget)
        widget_group.setLayout(group_layout)
        widget = widget_group
    # Data Type is a Scalar
    else:
        widget = QLineEdit()
        widget.setObjectName(f"{name.upper()}")

    return widget
