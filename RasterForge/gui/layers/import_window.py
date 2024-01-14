from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QDialog,
    QGridLayout,
    QPushButton,
    QLabel,
    QFrame,
    QSpinBox,
    QFileDialog,
    QCheckBox,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QScrollArea,
    QHBoxLayout,
    QComboBox,
    QProgressBar,
)

import rasterio

from RasterForge.containers.raster import Raster
from RasterForge.gui.data import data


class LayersImportWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Import Layers")
        self.layout = QGridLayout(self)
        self.setGeometry(100, 100, 500, 600)

        # Add Open File Button
        self.open_file_button = QPushButton("Open File")
        self.open_file_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.open_file_button, 0, 0, 1, 1)

        # Add File Explorer
        self.selected_file_label = QLabel("None")
        self.layout.addWidget(self.selected_file_label, 0, 1, 1, 23)

        # Add Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(separator, 1, 0, 1, 25)

        # Add Scale / Metadata / Geographic Transform Input
        scale_layout = QHBoxLayout()

        self.scale_label = QLabel("Scale")
        scale_layout.addWidget(self.scale_label, alignment=Qt.AlignRight)

        self.scale_spinbox = QSpinBox()
        self.scale_spinbox.setMinimum(1)
        self.scale_spinbox.setMaximum(100000)
        if data.raster is not None:
            self.scale_spinbox.setValue(data.raster.scale)
            self.scale_spinbox.setEnabled(False)
        else:
            self.scale_spinbox.setValue(1)
            self.scale_spinbox.setEnabled(True)
        scale_layout.addWidget(self.scale_spinbox, stretch=1)

        self.layout.addLayout(scale_layout, 2, 0, 1, 2)

        # Add Bands Checklist
        self.bands_label = QLabel("Bands")
        self.layout.addWidget(self.bands_label, 3, 0, 1, 1)

        # Create Checklist Scroll Area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area, 4, 0, 45, 25)

        self.band_checkboxes = []

        # Add Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(True)
        self.layout.addWidget(self.progress_bar, 49, 0, 1, 24)

        # Add Import Button
        self.import_button = QPushButton("Import")
        self.import_button.clicked.connect(self.submit_import_request)
        self.layout.addWidget(self.import_button, 49, 24, 1, 1)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("TIFF Files (*.tif)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_() == QFileDialog.Accepted:
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                self.selected_file_path = file_paths[0]
                self.selected_file_label.setText(f"{self.selected_file_path}")

                with rasterio.open(self.selected_file_path) as dataset:
                    num_bands = dataset.count
                    self.populate_bands_checklist(num_bands)

    def populate_bands_checklist(self, num_bands):
        # Clear Existing Checkboxes, Line Edits, and Combo Boxes
        for checkbox, line_edit, combo_box in self.band_checkboxes:
            checkbox.setParent(None)
            line_edit.setParent(None)
            combo_box.setParent(None)

        self.band_checkboxes = []

        # Add Checkboxes, Line Edits, and Combo Boxes
        for i in range(num_bands):
            # Create a Horizontal Layout for Each Band
            band_layout = QHBoxLayout()

            checkbox = QCheckBox()
            line_edit = QLineEdit(f"Band {i + 1}")
            combo_box = QComboBox()
            combo_box.addItems(["Relative", "Absolute"])

            # Add Widgets to the Horizontal Layout
            band_layout.addWidget(checkbox)
            band_layout.addWidget(line_edit)
            band_layout.addWidget(combo_box)

            # Add the Horizontal Layout to the Scroll Layout
            self.scroll_layout.addLayout(band_layout)

            self.band_checkboxes.append((checkbox, line_edit, combo_box))

        self.scroll_layout.setAlignment(Qt.AlignTop)

    def submit_import_request(self):
        selected_layers = []

        if data.raster is None:
            data.raster = Raster(scale=self.scale_spinbox.value())

        for index, (checkbox, line_edit, combo_box) in enumerate(self.band_checkboxes):
            if checkbox.isChecked():
                band_name = line_edit.text()
                data_type = combo_box.currentText()

                selected_layers.append(
                    {"id": index + 1, "name": band_name, "type": data_type.lower()}
                )

        if selected_layers is not {}:
            data.raster.import_layers(self.selected_file_path, selected_layers)
            data.raster_changed.emit()
