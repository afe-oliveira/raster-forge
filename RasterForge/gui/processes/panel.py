from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea, QStackedWidget

from RasterForge.composites.composite_finder import _find_composites
from RasterForge.gui.processes.composites_panel import CompositesPanel
from RasterForge.gui.processes.indices_panel import IndicesPanel
from RasterForge.indices.index_finder import _find_indices

from RasterForge.gui.data import data

class ProcessPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        # Panel 1: Main Process Panel
        main_process_panel = QWidget(self)
        main_process_layout = QVBoxLayout(main_process_panel)
        main_process_layout.setAlignment(Qt.AlignTop)

        composites_button = QPushButton(f'Composites', self)
        composites_button.clicked.connect(self.composites_clicked)
        main_process_layout.addWidget(composites_button)

        indices_button = QPushButton(f'Indices', self)
        indices_button.clicked.connect(self.indices_clicked)
        main_process_layout.addWidget(indices_button)

        topo_button = QPushButton(f'Topographical Features', self)
        topo_button.clicked.connect(self.topographical_clicked)
        main_process_layout.addWidget(topo_button)

        self.stacked_widget.addWidget(main_process_panel)
        data.process_main.connect(self.show_main_panel)

        # Panel 2: Composites Panel
        print(_find_composites())
        self.composites_panel = CompositesPanel(_find_composites())
        self.stacked_widget.addWidget(self.composites_panel)

        # Panel 3: Indices Panel
        self.indices_panel = IndicesPanel(_find_indices())
        self.stacked_widget.addWidget(self.indices_panel)

        # Panel 4: Topographical Features Panel
        self.topo_panel = CompositesPanel(_find_indices())
        self.stacked_widget.addWidget(self.topo_panel)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

    def show_main_panel(self):
        self.stacked_widget.setCurrentIndex(0)

    def composites_clicked(self):
        self.stacked_widget.setCurrentIndex(1)

    def indices_clicked(self):
        self.stacked_widget.setCurrentIndex(2)

    def topographical_clicked(self):
        self.stacked_widget.setCurrentIndex(2)

