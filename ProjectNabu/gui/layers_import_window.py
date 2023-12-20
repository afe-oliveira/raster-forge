from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QGridLayout, QPushButton, QLabel, QFrame,
    QSpinBox, QFileDialog, QCheckBox, QVBoxLayout, QWidget, QLineEdit, QScrollArea, QHBoxLayout
)

import rasterio

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

        # Add Scale / Metadata Input
        scale_layout = QHBoxLayout()

        self.scale_label = QLabel("Scale")
        scale_layout.addWidget(self.scale_label, alignment=Qt.AlignRight)

        self.scale_spinbox = QSpinBox()
        self.scale_spinbox.setMinimum(1)
        self.scale_spinbox.setMaximum(100000)
        self.scale_spinbox.setValue(1)
        scale_layout.addWidget(self.scale_spinbox, stretch=1)

        self.layout.addLayout(scale_layout, 2, 0, 1, 2) 

        self.metadata_checkbox = QCheckBox(f"Metadata")
        self.layout.addWidget(self.metadata_checkbox, 2, 24, 1, 1)

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

        # Add Import Button
        self.import_button = QPushButton("Import")
        # self.open_file_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.import_button, 49, 24, 1, 1)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("TIFF Files (*.tif)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_() == QFileDialog.Accepted:
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                selected_file_path = file_paths[0]
                self.selected_file_label.setText(f"{selected_file_path}")

                with rasterio.open(selected_file_path) as dataset:
                    num_bands = dataset.count
                    self.populate_bands_checklist(num_bands)

    def populate_bands_checklist(self, num_bands):
        # Clear Existing Checkboxes
        for checkbox in self.band_checkboxes:
            checkbox[0].setParent(None)
            checkbox[1].setParent(None)

        self.band_checkboxes = []

        # Add Checkboxes
        for i in range(num_bands):
            checkbox = QCheckBox(f"Band {i + 1}")
            line_edit = QLineEdit(f"Band {i + 1}")
            self.band_checkboxes.append((checkbox, line_edit))
            self.scroll_layout.addWidget(checkbox)
            self.scroll_layout.addWidget(line_edit)