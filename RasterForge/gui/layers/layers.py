from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget, QHBoxLayout,
)

from RasterForge.gui.common.layer_information import _LayerInfoWindow
from RasterForge.gui.data import _data

from .import_layers import _LayersImportWindow


class _LayersPanel(QWidget):
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
        self.import_layers_button.setToolTip("Import Layers from File")
        self.import_layers_button.setIcon(QIcon(":/icons/map-plus.svg"))
        self.import_layers_button.setObjectName("push-button")
        self.import_layers_button.clicked.connect(self.import_layers_clicked)
        self.layout.addWidget(self.import_layers_button, 0, 8, 1, 2, alignment=Qt.AlignRight)

        # Create and Layers List
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
                layer = _LayerElement(key)
                self.list_layout.addWidget(layer)

        # Set the Alignment
        self.list_layout.setAlignment(Qt.AlignTop)

    def import_layers_clicked(self):
        import_dialog = _LayersImportWindow(self)
        import_dialog.exec_()


class _LayerElement(QWidget):

    name = None

    def __init__(self, name):
        super().__init__()
        self.name = name

        self.layout = QGridLayout(self)
        self.setObjectName("layer-item")

        # Add Layer Name Label
        self.label = QLabel(self.name)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label.setObjectName("simple-label")
        self.layout.addWidget(self.label, 0, 0, 1, 1)

        # Create a Horizontal Layout for Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(1)
        button_layout.setAlignment(Qt.AlignRight)

        # View Button
        v_button = QPushButton()
        v_button.setToolTip("Show Layer")
        v_button.setIcon(QIcon(":/icons/eye.svg"))
        v_button.setObjectName("mini-push-button")
        v_button.clicked.connect(self._view_callback)
        button_layout.addWidget(v_button)

        # Edit Button
        edit_button = QPushButton()
        edit_button.setToolTip("Change Name")
        edit_button.setIcon(QIcon(":/icons/edit.svg"))
        edit_button.setObjectName("mini-push-button")
        edit_button.clicked.connect(self._edit_callback)
        button_layout.addWidget(edit_button)

        # Info Button
        info_button = QPushButton()
        info_button.setToolTip("Show Information")
        info_button.setIcon(QIcon(":/icons/info-square-rounded.svg"))
        info_button.setObjectName("mini-push-button")
        info_button.clicked.connect(self._info_callback)
        button_layout.addWidget(info_button)

        # Delete Button
        d_button = QPushButton()
        d_button.setToolTip("Delete Layer")
        d_button.setIcon(QIcon(":/icons/trash-x.svg"))
        d_button.setObjectName("mini-push-button")
        d_button.clicked.connect(self._delete_callback)
        button_layout.addWidget(d_button)

        # Add the Button Layout to the Main Grid Layout
        self.layout.addLayout(button_layout, 0, 1, 1, 1)

        self.edit_line = None  # Placeholder for Edit Functionality

    def _view_callback(self):
        _data.viewer = _data.raster.layers[self.name]
        _data.viewer_changed.emit()

    def _edit_callback(self):
        self.edit_line = QLineEdit(self.name)
        self.edit_line.setObjectName("edit-line")
        self.layout.replaceWidget(self.label, self.edit_line)
        self.label.setParent(None)

        self.edit_line.editingFinished.connect(self._edit_finished)

        self.edit_line.setFocus()

    def _edit_finished(self):
        new_name = self.edit_line.text().replace('\n', '')
        if new_name != self.name:
            _data.raster.edit_layer(self.name, new_name)
            _data.raster_changed.emit()

        self.layout.replaceWidget(self.edit_line, self.label)
        self.edit_line.setParent(None)

    def _info_callback(self):
        info_window = _LayerInfoWindow(self.name, _data.raster.layers[self.name], self)
        info_window.exec_()

    def _delete_callback(self):
        _data.raster.remove_layer(self.name)
        _data.raster_changed.emit()
