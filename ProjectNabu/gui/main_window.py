from PySide6.QtWidgets import QGridLayout, QWidget, QMainWindow, QVBoxLayout, QFrame, QPushButton

from .layers.panel import LayersPanel
from ProjectNabu.gui.viewer.panel import ViewerPanel
from .processes.panel import ProcessPanel


class OuterFrame(QFrame):
    def __init__(self, widget):
        super().__init__()
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        layout = QVBoxLayout(self)
        layout.addWidget(widget)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide 6 Application")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        panels = {
            'layers': OuterFrame(LayersPanel()),
            'processes': OuterFrame(ProcessPanel()),
            'viewer': OuterFrame(ViewerPanel())
        }

        grid_layout = QGridLayout(central_widget)
        grid_layout.addWidget(panels['layers'], 0, 0, 50, 40)
        grid_layout.addWidget(panels['processes'], 50, 0, 50, 40)
        grid_layout.addWidget(panels['viewer'], 0, 40, 100, 60)

        # Lock Proportions
        for i in range(100):
            grid_layout.setRowStretch(i, 1)
        for i in range(100):
            grid_layout.setColumnStretch(i, 1)