from typing import Any, Type

import numpy as np
from PySide6.QtWidgets import QComboBox, QVBoxLayout, QGroupBox, QLabel, QLineEdit

from RasterForge.gui.data import data


def adaptative_input(name: str, type: Type):
    widget = None

    # Data Type is an Numpy Array
    if type == np.ndarray:
        widget = QComboBox()
        if data.raster is not None:
            keys_from_raster = list(data.raster.layers.keys())
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
