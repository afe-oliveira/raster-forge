import os

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, Qt, QPainter, QIcon
from PySide6.QtSvg import QSvgRenderer


def _get_icon(svg_path: str, size: tuple[int, int] = (10, 10)):
    svg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), svg_path)
    icon = QIcon(svg_path)

    return icon


ADD_LAYER_ICON = _get_icon("map-plus.svg")

VIEW_LAYER_ICON = _get_icon("eye.svg")
EDIT_LAYER_ICON = _get_icon("edit.svg")
INFO_LAYER_ICON = _get_icon("info-square-rounded.svg")
DELETE_LAYER_ICON = _get_icon("trash-x.svg")