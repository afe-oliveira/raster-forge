from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLayout, QFrame, QGridLayout, \
    QScrollArea, QDialog
from .data import layer_data
from .layers_import_window import LayersImportWindow
from .show_matadata_window import MetadataWindow


class LayersPanel(QWidget):

    layer_data_changed = Signal()

    def __init__(self):
        super().__init__()

        self.layer_data_changed.connect(self.update_layers)

        self.layout = QGridLayout(self)

        # Inner Title Panel Label
        self.layout.addWidget(QLabel("Layers"), 0, 0, 1, 5)

        # Add the Projection, Transform and Metadata Buttons
        self.metadata_button = QPushButton("Metadata")
        self.transform_button = QPushButton("Transform")
        self.projection_button = QPushButton("Projection")

        self.layout.addWidget(self.metadata_button, 0, 5, 1, 1)
        self.layout.addWidget(self.transform_button, 0, 6, 1, 1)
        self.layout.addWidget(self.projection_button, 0, 7, 1, 1)

        self.metadata_button.clicked.connect(self.show_metadata_clicked)
        self.transform_button.clicked.connect(self.show_transform_clicked)
        self.projection_button.clicked.connect(self.show_projection_clicked)

        # Add the Import Layers Button
        self.import_layers_button = QPushButton("Import Layers")
        self.import_layers_button.clicked.connect(self.import_layers_clicked)
        self.layout.addWidget(self.import_layers_button, 0, 8, 1, 2)

        # Add Layers List
        self.scroll_list = QScrollArea(self)
        self.scroll_list.setWidgetResizable(True)

        self.list_widget = QWidget(self.scroll_list)
        self.list_layout = QVBoxLayout(self.list_widget)

        self.update_layers()

        self.scroll_list.setWidget(self.list_widget)
        self.layout.addWidget(self.scroll_list, 2, 0, 18, 10)

    def update_layers(self):
        # Clear existing layers
        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().setParent(None)

        # Add updated layers
        for key, value in layer_data.layers.items():
            layer = LayerElement(key)
            self.list_layout.addWidget(layer)

    def import_layers_clicked(self):
        import_dialog = LayersImportWindow(self)
        import_dialog.layer_data_changed.connect(self.layer_data_changed)
        result = import_dialog.exec_()
        if result == QDialog.Accepted:
            self.update_layers()

    def show_metadata_clicked(self):
        metadata_window = MetadataWindow(layer_data.metadata)
        metadata_window.exec_()

    def show_transform_clicked(self):
        pass

    def show_projection_clicked(self):
        pass


class LayerElement(QWidget):

    name = None

    def __init__(self, name):
        super().__init__()
        self.name = name

        layout = QGridLayout(self)

        layout.addWidget(QLabel(self.name), 0, 0, 1, 7)
        layout.addWidget(QPushButton("V"), 0, 8, 1, 1)
        layout.addWidget(QPushButton("E"), 0, 9, 1, 1)
        layout.addWidget(QPushButton("D"), 0, 10, 1, 1)
