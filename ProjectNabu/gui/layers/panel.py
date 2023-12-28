from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLayout, QFrame, QGridLayout, \
    QScrollArea, QDialog, QLineEdit
from ProjectNabu.gui.data import data
from .import_window import LayersImportWindow
from .info_window import LayerInfoWindow


class LayersPanel(QWidget):

    def __init__(self):
        super().__init__()

        data.raster_changed.connect(self.update_layers)

        self.layout = QGridLayout(self)

        # Inner Title Panel Label
        self.layout.addWidget(QLabel("Layers"), 0, 0, 1, 5)

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
        # Clear Existing Layers
        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().setParent(None)

        # Add Updated Layers
        if data.raster is not None:
            for key, value in data.raster.layers.items():
                layer = LayerElement(key)
                self.list_layout.addWidget(layer)

        # Set the Alignment
        self.list_layout.setAlignment(Qt.AlignTop)

    def import_layers_clicked(self):
        import_dialog = LayersImportWindow(self)
        import_dialog.exec_()


class LayerElement(QWidget):

    name = None

    def __init__(self, name):
        super().__init__()
        self.name = name

        self.layout = QGridLayout(self)

        self.label = QLabel(self.name)
        self.layout.addWidget(self.label, 0, 0, 1, 16)

        # View Button
        v_button = QPushButton("V")
        v_button.clicked.connect(self.handle_view_button_click)
        self.layout.addWidget(v_button, 0, 17, 1, 1)

        # Edit Button
        self.edit_button = QPushButton("E")
        self.edit_button.clicked.connect(self.handle_edit_button_click)
        self.layout.addWidget(self.edit_button, 0, 18, 1, 1)

        # Info Button
        self.info_button = QPushButton("I")
        self.info_button.clicked.connect(self.handle_info_button_click)
        self.layout.addWidget(self.info_button, 0, 19, 1, 1)

        # Delete Button
        d_button = QPushButton("D")
        d_button.clicked.connect(self.handle_delete_button_click)
        self.layout.addWidget(d_button, 0, 20, 1, 1)

        self.edit_line = None  # Placeholder for QLineEdit

    def handle_view_button_click(self):
        data.viewer = data.raster.layers[self.name]
        data.viewer_changed.emit()

    def handle_edit_button_click(self):
        self.edit_line = QLineEdit(self.name)
        self.layout.replaceWidget(self.label, self.edit_line)
        self.label.setParent(None)

        self.edit_line.editingFinished.connect(self.handle_edit_finished)

        self.edit_line.setFocus()

    def handle_edit_finished(self):
        new_name = self.edit_line.text()
        if new_name != self.name:
            data.raster.edit_layer(self.name, new_name)
            data.raster_changed.emit()

        self.layout.replaceWidget(self.edit_line, self.label)
        self.edit_line.setParent(None)

    def handle_info_button_click(self):
        info_window = LayerInfoWindow(self.name, self)
        info_window.exec_()

    def handle_delete_button_click(self):
        data.raster.remove_layer(self.name)
        data.raster_changed.emit()
