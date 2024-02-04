from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from .viewer.viewer import _ViewerPanel
from .layers.layers import _LayersPanel
from .processes.processes import _ProcessPanel


class _OuterFrame(QFrame):
    def __init__(self, widget):
        super().__init__()

        # Set Panel Style Name
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.setObjectName("outer-panel")

        # Create Vertical Layout and Add Child Widget
        layout = QVBoxLayout(self)
        layout.addWidget(widget)


class _MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Window Title and Icon
        self.setWindowTitle("Raster Forge")
        self.setWindowIcon(
            QIcon(
                QPixmap(":/icons/logo-flat.svg").scaledToHeight(
                    64, Qt.SmoothTransformation
                )
            )
        )
        self.setGeometry(100, 100, 1200, 800)

        # Create Main Widget and Set Style Name
        central_widget = QWidget(self)
        self.setObjectName("main-window")
        self.setCentralWidget(central_widget)

        # Set Component Panels
        panels = {
            "layers": _OuterFrame(_LayersPanel()),
            "processes": _OuterFrame(_ProcessPanel()),
            "viewer": _OuterFrame(_ViewerPanel()),
        }

        # Lay Panels in a Grid Layout
        grid_layout = QGridLayout(central_widget)
        grid_layout.addWidget(panels["layers"], 0, 0, 50, 40)
        grid_layout.addWidget(panels["processes"], 50, 0, 50, 40)
        grid_layout.addWidget(panels["viewer"], 0, 40, 100, 60)

        # Lock Proportions
        for i in range(100):
            grid_layout.setRowStretch(i, 1)
        for i in range(100):
            grid_layout.setColumnStretch(i, 1)
