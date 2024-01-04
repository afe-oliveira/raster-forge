from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTabWidget, QWidget, QGridLayout, QSizePolicy

from RasterForge.gui.data import data

class LayerInfoWindow(QDialog):
    def __init__(self, layer_name, parent=None):
        super().__init__(parent)
        self.name = layer_name
        self.setWindowTitle(f"Layer Information - {self.name}")

        # Create a layout for the information window
        main_layout = QVBoxLayout(self)

        # Create a tab widget
        self.tab_widget = QTabWidget(self)

        # Add tabs for metadata, transform, projection, and statistics
        self.tab_widget.addTab(self.metadata_tab(), "Metadata")
        self.tab_widget.addTab(self.transform_tab(), "Transform")
        self.tab_widget.addTab(self.projection_tab(), "Projection")
        self.tab_widget.addTab(self.statistics_tab(), "Statistics")

        # Add the tab widget to the main layout
        main_layout.addWidget(self.tab_widget)

        # Set a predefined window size
        self.setFixedSize(500, 400)  # Adjust the values as needed

    def metadata_tab(self):
        metadata_tab = QWidget()
        metadata_tab.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        metadata_layout = QVBoxLayout(metadata_tab)
        metadata_layout.setAlignment(Qt.AlignTop)

        metadata_dict = data.raster.layers[self.name].metadata
        del metadata_dict['crs']
        del metadata_dict['transform']

        grid_layout = QGridLayout()
        row = 0
        for key, value in metadata_dict.items():
            key_label = QLabel(str(key).upper())
            value_label = QLabel(str(value).upper())

            key_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            grid_layout.addWidget(key_label, row, 0)
            grid_layout.addWidget(value_label, row, 1)

            row += 1

        metadata_layout.addLayout(grid_layout)
        return metadata_tab

    def transform_tab(self):
        transform_tab = QWidget()
        transform_layout = QVBoxLayout(transform_tab)
        transform_label = QLabel("Transform: ...")  # Replace "..." with actual transform information
        transform_layout.addWidget(transform_label)
        return transform_tab

    def projection_tab(self):
        projection_tab = QWidget()
        projection_layout = QVBoxLayout(projection_tab)
        projection_label = QLabel("Projection: ...")  # Replace "..." with actual projection information
        projection_layout.addWidget(projection_label)
        return projection_tab

    def statistics_tab(self):
        statistics_tab = QWidget()
        statistics_layout = QVBoxLayout(statistics_tab)
        statistics_label = QLabel("Statistics: ...")  # Replace "..." with actual statistics information
        statistics_layout.addWidget(statistics_label)
        return statistics_tab
