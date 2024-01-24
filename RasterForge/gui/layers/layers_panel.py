from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from RasterForge.gui.common.layer_information import LayerInfoWindow
from RasterForge.gui.data import _data

from .import_layers_window import LayersImportWindow

from RasterForge.icons.icons import *


class LayersPanel(QWidget):
    def __init__(self):
        super().__init__()

        _data.raster_changed.connect(self.update_layers)

        self.layout = QGridLayout(self)

        # Inner Title Panel Label
        title_label = QLabel("Layers")
        title_label.setObjectName("title-label")
        self.layout.addWidget(title_label, 0, 0, 1, 5)

        # Add the Import Layers Button
        self.import_layers_button = QPushButton()
        self.import_layers_button.setToolTip("Import layers from external file.")
        self.import_layers_button.setIcon(ADD_LAYER_ICON)
        self.import_layers_button.setObjectName("simple-button")
        self.import_layers_button.clicked.connect(self.import_layers_clicked)
        self.layout.addWidget(self.import_layers_button, 0, 8, 1, 2, alignment=Qt.AlignRight)

        # Add Layers List
        self.scroll_list = QScrollArea(self)
        self.scroll_list.setWidgetResizable(True)
        self.scroll_list.setObjectName("scroll-list")

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
        if _data.raster is not None:
            for key, value in _data.raster.layers.items():
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
        self.setObjectName("layer-item")

        self.label = QLabel(self.name)
        self.label.setObjectName("simple-label")
        self.layout.addWidget(self.label, 0, 0, 1, 16)

        # View Button
        v_button = QPushButton()
        v_button.setToolTip("Show layer.")
        v_button.setIcon(VIEW_LAYER_ICON)
        v_button.setObjectName("simple-button-small")
        v_button.clicked.connect(self.handle_view_button_click)
        self.layout.addWidget(v_button, 0, 17, 1, 1)

        # Edit Button
        edit_button = QPushButton("E")
        edit_button.setToolTip("Change layer name.")
        edit_button.setIcon(EDIT_LAYER_ICON)
        edit_button.setObjectName("simple-button-small")
        edit_button.clicked.connect(self.handle_edit_button_click)
        self.layout.addWidget(edit_button, 0, 18, 1, 1)

        # Info Button
        info_button = QPushButton("I")
        info_button.setToolTip("Show additional layer information.")
        info_button.setIcon(INFO_LAYER_ICON)
        info_button.setObjectName("simple-button-small")
        info_button.clicked.connect(self.handle_info_button_click)
        self.layout.addWidget(info_button, 0, 19, 1, 1)

        # Delete Button
        d_button = QPushButton("D")
        d_button.setToolTip("Delete layer.")
        d_button.setIcon(DELETE_LAYER_ICON)
        d_button.setObjectName("simple-button-small")
        d_button.clicked.connect(self.handle_delete_button_click)
        self.layout.addWidget(d_button, 0, 20, 1, 1)

        self.edit_line = None  # Placeholder for Edit Functionality

    def handle_view_button_click(self):
        _data.viewer = _data.raster.layers[self.name]
        _data.viewer_changed.emit()

    def handle_edit_button_click(self):
        self.edit_line = QLineEdit(self.name)
        self.layout.replaceWidget(self.label, self.edit_line)
        self.label.setParent(None)

        self.edit_line.editingFinished.connect(self.handle_edit_finished)

        self.edit_line.setFocus()

    def handle_edit_finished(self):
        new_name = self.edit_line.text()
        if new_name != self.name:
            _data.raster.edit_layer(self.name, new_name)
            _data.raster_changed.emit()

        self.layout.replaceWidget(self.edit_line, self.label)
        self.edit_line.setParent(None)

    def handle_info_button_click(self):
        info_window = LayerInfoWindow(self.name, _data.raster.layers[self.name], self)
        info_window.exec_()

    def handle_delete_button_click(self):
        _data.raster.remove_layer(self.name)
        _data.raster_changed.emit()
