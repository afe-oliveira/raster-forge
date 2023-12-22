from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLayout, QFrame, QGridLayout, \
    QScrollArea, QDialog, QLineEdit
from ProjectNabu.gui.data import layer_data
from .import_window import LayersImportWindow


class LayersPanel(QWidget):

    layer_data_changed = Signal()

    def __init__(self):
        super().__init__()

        self.layer_data_changed.connect(self.update_layers)

        self.layout = QGridLayout(self)

        # Inner Title Panel Label
        self.layout.addWidget(QLabel("Layers"), 0, 0, 1, 5)

        # Add the Projection, Transform and Metadata Buttons
        self.transform_button = QPushButton("Transform")
        self.projection_button = QPushButton("Projection")

        self.layout.addWidget(self.transform_button, 0, 6, 1, 1)
        self.layout.addWidget(self.projection_button, 0, 7, 1, 1)

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
        # Clear Existing Layers
        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().setParent(None)

        # Add Updated Layers
        for key, value in layer_data.layers.items():
            layer = LayerElement(key, self.layer_data_changed)
            self.list_layout.addWidget(layer)

    def import_layers_clicked(self):
        import_dialog = LayersImportWindow(self)
        import_dialog.layer_data_changed.connect(self.layer_data_changed)
        import_dialog.exec_()

    def show_transform_clicked(self):
        pass

    def show_projection_clicked(self):
        pass



class LayerElement(QWidget):

    name = None
    layer_data_changed = Signal()

    def __init__(self, name, layer_data_changed):
        super().__init__()
        self.name = name
        self.layer_data_changed.connect(layer_data_changed)

        self.layout = QGridLayout(self)

        self.label = QLabel(self.name)
        self.layout.addWidget(self.label, 0, 0, 1, 7)

        # View Button
        v_button = QPushButton("V")
        v_button.clicked.connect(self.handle_view_button_click)
        self.layout.addWidget(v_button, 0, 8, 1, 1)

        # Edit Button
        self.edit_button = QPushButton("E")
        self.edit_button.clicked.connect(self.handle_edit_button_click)
        self.layout.addWidget(self.edit_button, 0, 9, 1, 1)

        # Delete Button
        d_button = QPushButton("D")
        d_button.clicked.connect(self.handle_delete_button_click)
        self.layout.addWidget(d_button, 0, 10, 1, 1)

        self.edit_line = None  # Placeholder for QLineEdit

    def handle_view_button_click(self):
        print(f'View button clicked for {self.name}')

    def handle_edit_button_click(self):
        self.edit_line = QLineEdit(self.name)
        self.layout.replaceWidget(self.label, self.edit_line)
        self.label.setParent(None)

        self.edit_line.editingFinished.connect(self.handle_edit_finished)

        self.edit_line.setFocus()

    def handle_edit_finished(self):
        new_name = self.edit_line.text()
        if new_name != self.name:
            layer_data.edit_layer(self.name, new_name)
            self.layer_data_changed.emit()

        self.layout.replaceWidget(self.edit_line, self.label)
        self.edit_line.setParent(None)

    def handle_delete_button_click(self):
        layer_data.remove_layer(self.name)
        self.layer_data_changed.emit()
