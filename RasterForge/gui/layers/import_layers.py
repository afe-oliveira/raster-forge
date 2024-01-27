import rasterio
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QFileDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from RasterForge.containers.raster import Raster
from RasterForge.gui.data import _data


class _LayersImportWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Import Layers")
        self.layout = QVBoxLayout(self)

        # File Interaction Layout
        file_layout = QHBoxLayout()

        # Add File Explorer
        selected_file_label = QLabel("No File Selected")
        selected_file_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        selected_file_label.setObjectName("simple-label")
        file_layout.addWidget(selected_file_label)

        # Add Open File Button
        open_file_button = QPushButton()
        open_file_button.setToolTip("Select File")
        open_file_button.setIcon(QIcon(":/icons/folder.svg"))
        open_file_button.setObjectName("push-button")
        open_file_button.clicked.connect(self._open_file_callback)
        file_layout.addWidget(open_file_button)

        self.layout.addLayout(file_layout)

        # Add Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(separator)

        # Add Scale Input
        scale_layout = QHBoxLayout()

        scale_label = QLabel("Scale")
        scale_label.setObjectName("simple-label-no-bg")
        scale_label.setToolTip("Scale is the Side Length of Each Cell (in Meters)")
        scale_layout.addWidget(scale_label, alignment=Qt.AlignRight)

        self.scale_spinbox = QSpinBox()
        self.scale_spinbox.setObjectName("spin-box")
        self.scale_spinbox.setMinimum(1)
        self.scale_spinbox.setMaximum(100000)
        if _data.raster is not None:
            self.scale_spinbox.setValue(_data.raster.scale)
            self.scale_spinbox.setEnabled(False)
        else:
            self.scale_spinbox.setValue(1)
            self.scale_spinbox.setEnabled(True)
        scale_layout.addWidget(self.scale_spinbox, stretch=1)

        self.layout.addLayout(scale_layout)

        # Add Bands Checklist
        bands_label = QLabel("Bands")
        bands_label.setObjectName("title-label")
        self.layout.addWidget(bands_label)

        # Create Checklist Scroll Area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll-list")
        self.scroll_area.setMinimumSize(500, 450)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout.addWidget(self.scroll_area)

        self.band_checkboxes = []

        # Bottom Layout
        bottom_layout = QHBoxLayout()

        # Add Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(True)
        bottom_layout.addWidget(self.progress_bar)

        # Add Import Button
        import_button = QPushButton("Import")
        import_button.setObjectName("push-button-text")
        import_button.clicked.connect(self._import_callback)
        bottom_layout.addWidget(import_button)

        self.layout.addLayout(bottom_layout)

    def _open_file_callback(self):
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
                    self._populate_bands_checklist(num_bands)

    def _populate_bands_checklist(self, num_bands):
        # Clear Existing items
        for checkbox, line_edit in self.band_checkboxes:
            checkbox.setParent(None)
            line_edit.setParent(None)

        self.band_checkboxes = []

        # Add Checkboxes, Line Edits, and Combo Boxes
        for i in range(num_bands):
            # Create a Horizontal Layout for Each Band
            band_layout = QHBoxLayout()

            checkbox = QCheckBox()
            line_edit = QLineEdit(f"Band {i + 1}")
            line_edit.setObjectName("edit-line")

            # Add Widgets to the Horizontal Layout
            band_layout.addWidget(checkbox)
            band_layout.addWidget(line_edit)

            # Add the Horizontal Layout to the Scroll Layout
            self.scroll_layout.addLayout(band_layout)

            self.band_checkboxes.append((checkbox, line_edit))

        self.scroll_layout.setAlignment(Qt.AlignTop)

    def _import_callback(self):
        selected_layers = []

        if _data.raster is None:
            _data.raster = Raster(scale=self.scale_spinbox.value())

        for index, (checkbox, line_edit, combo_box) in enumerate(self.band_checkboxes):
            if checkbox.isChecked():
                band_name = line_edit.text()
                data_type = combo_box.currentText()

                selected_layers.append(
                    {"id": index + 1, "name": band_name, "type": data_type.lower()}
                )

        if selected_layers is not {}:
            _data.raster.import_layers(self.selected_file_path, selected_layers)
            _data.raster_changed.emit()
