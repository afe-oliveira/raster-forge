from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QScrollArea,
    QStackedWidget,
)

from RasterForge.gui.processes.composites_panel import CompositesPanel
from RasterForge.gui.processes.indices_panel import IndicesPanel
from RasterForge.gui.processes.topographical_panel import TopographicalPanel
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

        composites_button = QPushButton(f"Composites", self)
        composites_button.clicked.connect(self.composites_clicked)
        main_process_layout.addWidget(composites_button)

        indices_button = QPushButton(f"Indices", self)
        indices_button.clicked.connect(self.indices_clicked)
        main_process_layout.addWidget(indices_button)

        topo_button = QPushButton(f"Topographical Features", self)
        topo_button.clicked.connect(self.topographical_clicked)
        main_process_layout.addWidget(topo_button)

        distance_button = QPushButton(f"Distance Chart", self)
        distance_button.clicked.connect(self.distance_clicked())
        main_process_layout.addWidget(distance_button)

        fuel_button = QPushButton(f"Fuel Map", self)
        fuel_button.clicked.connect(self.fuel_clicked())
        main_process_layout.addWidget(fuel_button)

        self.stacked_widget.addWidget(main_process_panel)
        data.process_main.connect(self.show_main_panel)

        # Panel 2: Composites Panel
        self.composites_panel = CompositesPanel()
        self.stacked_widget.addWidget(self.composites_panel)

        # Panel 3: Indices Panel
        self.indices_panel = IndicesPanel(_find_indices())
        self.stacked_widget.addWidget(self.indices_panel)

        # Panel 4: Topographical Features Panel
        self.topo_panel = TopographicalPanel()
        self.stacked_widget.addWidget(self.topo_panel)

        # Panel 5: Distance Feature Panel
        self.distance_panel = TopographicalPanel()
        self.stacked_widget.addWidget(self.distance_panel)

        # Panel 6: Fuel Feature Panel
        self.fuel_panel = TopographicalPanel()
        self.stacked_widget.addWidget(self.fuel_panel)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

    def show_main_panel(self):
        self.stacked_widget.setCurrentIndex(0)

    def composites_clicked(self):
        self.stacked_widget.setCurrentIndex(1)

    def indices_clicked(self):
        self.stacked_widget.setCurrentIndex(2)

    def topographical_clicked(self):
        self.stacked_widget.setCurrentIndex(3)

    def distance_clicked(self):
        self.stacked_widget.setCurrentIndex(3)

    def fuel_clicked(self):
        self.stacked_widget.setCurrentIndex(3)
