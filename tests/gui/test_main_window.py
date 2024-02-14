from PySide6.QtCore import QRect
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow


def test_window_title(main_window: QMainWindow):
    assert main_window.windowTitle() == "Raster Forge"


def test_window_icon(main_window: QMainWindow):
    assert isinstance(main_window.windowIcon(), QIcon)


def test_window_geometry(main_window: QMainWindow):
    assert main_window.geometry() == QRect(100, 100, 1200, 800)


def test_layout(main_window: QMainWindow):
    layout = main_window.centralWidget().layout()

    assert layout.itemAtPosition(0, 0).widget().objectName() == "outer-panel"
    assert layout.itemAtPosition(50, 0).widget().objectName() == "outer-panel"
    assert layout.itemAtPosition(0, 40).widget().objectName() == "outer-panel"

