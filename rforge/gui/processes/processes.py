from PySide6 import QtCore
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from rforge.gui.data import _data
from rforge.gui.processes.panels.composites import _CompositesPanel
from rforge.gui.processes.panels.distance import _DistanceFieldPanel
from rforge.gui.processes.panels.fuel import _FuelMapPanel
from rforge.gui.processes.panels.height import _HeightPanel
from rforge.gui.processes.panels.indices import _IndicesPanel
from rforge.gui.processes.panels.topography import _TopographyPanel

GRID_BUTTON_SIZE = 100


class _ProcessPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        # Main Process Panel
        main_process_panel = QWidget(self)
        main_process_layout = QVBoxLayout(main_process_panel)
        main_process_layout.setAlignment(Qt.AlignTop)

        # Inner Title Panel Label
        title_label = QLabel("Processes")
        title_label.setObjectName("title-label")
        main_process_layout.addWidget(title_label)

        # Create Scroll Area
        self.scroll_area = QScrollArea(self)
        main_process_layout.addWidget(self.scroll_area)

        buttons_widget = QWidget(self)
        self.scroll_area.setWidget(buttons_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll-list")

        # Create Grid Layout for the Buttons
        self.grid_layout = QGridLayout(buttons_widget)
        self.grid_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.buttons = [
            ("Composites", ":/icons/stack-2.svg", self._composites_callback),
            (
                "Multispectral Indices",
                ":/icons/3d-cube-sphere.svg",
                self._indices_callback,
            ),
            ("Topography", ":/icons/mountain.svg", self._topographical_callback),
            ("Height Map", ":/icons/line-height.svg", self._height_callback),
            ("Distance Field", ":/icons/arrows-diagonal.svg", self._distance_callback),
            ("Fuel Map", ":/icons/flame.svg", self._fuel_callback),
        ]

        self._update_button_layout()

        self.stacked_widget.addWidget(main_process_panel)
        _data.process_main.connect(self._main_panel_callback)

        # Composites Panel
        self.composites_panel = _CompositesPanel(name="Composites", selector=True)
        self.stacked_widget.addWidget(self.composites_panel)

        # Indices Panel
        self.indices_panel = _IndicesPanel(name="Multispectral Indices", selector=True)
        self.stacked_widget.addWidget(self.indices_panel)

        # Topographical Features Panel
        self.topo_panel = _TopographyPanel(name="Topography", selector=True)
        self.stacked_widget.addWidget(self.topo_panel)

        # Height Panel
        self.height_panel = _HeightPanel(name="Height Map")
        self.stacked_widget.addWidget(self.height_panel)

        # Distance Chart Panel
        self.distance_panel = _DistanceFieldPanel(name="Distance Field")
        self.stacked_widget.addWidget(self.distance_panel)

        # Fuel Feature Panel
        self.fuel_panel = _FuelMapPanel(name="Distance Map")
        self.stacked_widget.addWidget(self.fuel_panel)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_button_layout()

    def _update_button_layout(self):
        def create_button(tooltip, icon_path, callback):
            button = QPushButton(self)
            button.setToolTip(tooltip)
            button.setIcon(QIcon(icon_path))
            button.setFixedSize(GRID_BUTTON_SIZE, GRID_BUTTON_SIZE)
            button.clicked.connect(callback)
            return button

        if self.scroll_area is None or self.scroll_area.viewport() is None:
            return

        # Calculate the Number of Buttons per Row
        available_width = self.scroll_area.viewport().size().width()
        if available_width <= 0:
            return
        max_buttons_per_row = max(1, available_width // GRID_BUTTON_SIZE)

        # Clear the Existing Layout
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Add Buttons to Grid
        row, col = 0, 0
        for text, icon_path, callback in self.buttons:
            try:
                if text is None or icon_path is None or callback is None:
                    continue
                button = create_button(text, icon_path, callback)
                self.grid_layout.addWidget(button, row, col)
                button.setIconSize(
                    QtCore.QSize(
                        int(GRID_BUTTON_SIZE * 0.75), int(GRID_BUTTON_SIZE * 0.75)
                    )
                )
                col += 1
                if col >= max_buttons_per_row:
                    col = 0
                    row += 1
            except Exception as e:
                print(e)

    def _main_panel_callback(self):
        self.stacked_widget.setCurrentIndex(0)

    def _composites_callback(self):
        self.stacked_widget.setCurrentIndex(1)

    def _indices_callback(self):
        self.stacked_widget.setCurrentIndex(2)

    def _topographical_callback(self):
        self.stacked_widget.setCurrentIndex(3)

    def _height_callback(self):
        self.stacked_widget.setCurrentIndex(4)

    def _distance_callback(self):
        self.stacked_widget.setCurrentIndex(5)

    def _fuel_callback(self):
        self.stacked_widget.setCurrentIndex(6)
