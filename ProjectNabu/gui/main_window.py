from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QGridLayout, QWidget, QMainWindow, QVBoxLayout, QLabel, QFrame, QPushButton

from .layers_panel import LayersPanel


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

        pannels = {
            'layers': OuterFrame(LayersPanel()),
            'processes': OuterFrame(QPushButton('Button 2')),
            'viewer': OuterFrame(QPushButton('Button 3'))
        }

        grid_layout = QGridLayout(central_widget)
        grid_layout.addWidget(pannels['layers'], 0, 0, 5, 8)
        grid_layout.addWidget(pannels['processes'], 5, 0, 5, 8)
        grid_layout.addWidget(pannels['viewer'], 0, 8, 10, 12)