import os
import shutil
import tempfile

import numpy as np
import rasterio
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QIcon, QImage, QPixmap, QTransform
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFileDialog,
    QFrame,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)
from rasterio.transform import from_origin

from RasterForge.gui.common.layer_information import _LayerInfoWindow
from RasterForge.gui.data import _data

from .save_operations import _save_as_geotiff, _save_as_image, _save_as_layer

COLORMAPS = {
    "Viridis": "viridis",
    "Viridis (Reversed)": "viridis_r",
    "Plasma": "plasma",
    "Plasma (Reversed)": "plasma_r",
    "Inferno": "inferno",
    "Inferno (Reversed)": "inferno_r",
    "Magma": "magma",
    "Magma (Reversed)": "magma_r",
    "Cividis": "cividis",
    "Cividis (Reversed)": "cividis_r",
    "Twilight": "twilight",
    "Twilight (Reversed)": "twilight_r",
    "Gray": "gray",
    "Gray (Reversed)": "gray_r",
    "Autumn": "autumn",
    "Autumn (Reversed)": "autumn_r",
    "Cool-Warm": "coolwarm",
    "Red-Blue": "RdBu",
    "Spectral": "Spectral",
    "Jet": "jet",
    "Ocean": "ocean",
    "Terrain": "terrain",
}


class _ViewerPanel(QWidget):

    current_zoom = 0
    layer = None

    def __init__(self):
        super().__init__()

        # Create Vertical Layout
        layout = QVBoxLayout(self)

        _data.viewer_changed.connect(self.update_viewer)

        # Create Horizontal Top Save/Control Bar Layout
        top_layout = QHBoxLayout(self)
        control_layout = QHBoxLayout(self)
        save_layout = QHBoxLayout(self)

        # Add Save Buttons
        self.save_layer_button = QPushButton("LAYER")
        self.save_layer_button.setToolTip("Save Data as Layer")
        self.save_layer_button.setIcon(QIcon(":/icons/device-floppy.svg"))
        self.save_layer_button.setObjectName("push-button-text")
        self.save_layer_button.setFixedWidth(80)
        save_layout.addWidget(self.save_layer_button)
        self.save_layer_button.clicked.connect(_save_as_layer)

        self.save_image_button = QPushButton("IMAGE")
        self.save_image_button.setToolTip("Save Data as Image (+ Colormap)")
        self.save_image_button.setIcon(QIcon(":/icons/device-floppy.svg"))
        self.save_image_button.setObjectName("push-button-text")
        self.save_image_button.setFixedWidth(80)
        save_layout.addWidget(self.save_image_button)

        self.save_tif_button = QPushButton("TIFF")
        self.save_tif_button.setToolTip("Save Data as GeoTIFF")
        self.save_tif_button.setIcon(QIcon(":/icons/device-floppy.svg"))
        self.save_tif_button.setObjectName("push-button-text")
        self.save_tif_button.setFixedWidth(80)
        save_layout.addWidget(self.save_tif_button)
        self.save_tif_button.clicked.connect(_save_as_geotiff)

        # Add Colormap ComboBox
        colormap_label = QLabel("Colormap:")
        colormap_label.setObjectName("simple-label-no-bg")
        self.colormap_combobox = QComboBox()
        self.colormap_combobox.addItems(list(COLORMAPS.keys()))
        self.colormap_combobox.setCurrentText("gray")
        control_layout.addWidget(colormap_label)
        control_layout.addWidget(self.colormap_combobox)
        self.colormap_combobox.currentIndexChanged.connect(self.update_viewer)
        self.save_image_button.clicked.connect(
            lambda: _save_as_image(COLORMAPS[self.colormap_combobox.currentText()])
        )

        # Add Pixel Value Button
        self.pixel_value_button = QCheckBox()
        self.pixel_value_button.setToolTip("Show Pixel Value")
        self.pixel_value_button.setObjectName("switch-toggle-pv")
        control_layout.addWidget(self.pixel_value_button)
        self.pixel_value_button.clicked.connect(self._pixel_values_toggle_callback)

        # Add Info Button
        self.info_button = QPushButton()
        self.info_button.setToolTip("Show Information")
        self.info_button.setIcon(QIcon(":/icons/info-square-rounded.svg"))
        self.info_button.setObjectName("push-button")
        control_layout.addWidget(self.info_button)
        self.info_button.clicked.connect(self.show_info)

        # Add Top Bar
        top_layout.addLayout(save_layout, Qt.AlignLeft)
        top_layout.addStretch(100)
        top_layout.addLayout(control_layout, Qt.AlignRight)
        layout.addLayout(top_layout, Qt.AlignTop)

        # Add Graphics Scene and Graphics View
        self.scene = QGraphicsScene(self)
        self.graphics_view = QGraphicsView(self.scene)
        self.graphics_view.setMouseTracking(True)
        layout.addWidget(self.graphics_view)

        self.graphics_view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

        # Add Zoom Slider
        self.zoom_slider = QSlider(Qt.Horizontal)
        self.zoom_slider.setMinimum(0)
        self.zoom_slider.setMaximum(2000)
        self.zoom_slider.setValue(0)
        self.zoom_slider.setObjectName("slider")

        self.zoom_label = QLabel("Zoom")
        self.zoom_label.setObjectName("simple-label-no-bg")
        self.zoom_value_label = QLabel("1.0")
        self.zoom_value_label.setObjectName("simple-label")
        self.restore_zoom_button = QPushButton()
        self.restore_zoom_button.setToolTip("Reset Zoom")
        self.restore_zoom_button.setIcon(QIcon(":/icons/zoom-reset.svg"))
        self.restore_zoom_button.setObjectName("push-button")

        zoom_layout = QHBoxLayout(self)
        zoom_layout.addWidget(self.zoom_label)
        zoom_layout.addWidget(self.zoom_slider)
        zoom_layout.addWidget(self.zoom_value_label)
        zoom_layout.addWidget(self.restore_zoom_button)
        layout.addLayout(zoom_layout)

        self.zoom_slider.valueChanged.connect(self.update_zoom)
        self.restore_zoom_button.clicked.connect(self.restore_zoom)

        # Add a Separator
        separator_line = QFrame()
        separator_line.setFrameShape(QFrame.HLine)
        separator_line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator_line)

        # Add Coordinate Display
        coordinates_layout = QHBoxLayout(self)
        pixel_coordinates_layout = QHBoxLayout(self)
        real_coordinates_layout = QHBoxLayout(self)

        self.pixel_coordinates_x = QLabel("N/A")
        self.pixel_coordinates_x.setToolTip("X Value (Pixels)")
        self.pixel_coordinates_x.setObjectName("simple-label")
        self.pixel_coordinates_y = QLabel("N/A")
        self.pixel_coordinates_y.setToolTip("Y Value (Pixels)")
        self.pixel_coordinates_y.setObjectName("simple-label")
        pixel_coordinates_layout.addWidget(self.pixel_coordinates_x)
        pixel_coordinates_layout.addWidget(self.pixel_coordinates_y)

        self.lat_coordinates_label = QLabel("N/A")
        self.lat_coordinates_label.setToolTip("Latitude")
        self.lat_coordinates_label.setObjectName("simple-label")
        self.lng_coordinates_label = QLabel("N/A")
        self.lng_coordinates_label.setToolTip("Longitude")
        self.lng_coordinates_label.setObjectName("simple-label")
        real_coordinates_layout.addWidget(self.lat_coordinates_label)
        real_coordinates_layout.addWidget(self.lng_coordinates_label)

        coordinates_layout.addLayout(pixel_coordinates_layout, Qt.AlignLeft)
        coordinates_layout.addStretch(100)
        coordinates_layout.addLayout(real_coordinates_layout, Qt.AlignRight)
        layout.addLayout(coordinates_layout)

        # Initialize a Label for Displaying Pixel Values
        self.band_values_label = QLabel("", self)
        self.band_values_label.setObjectName("simple-label")
        self.band_values_label.setAlignment(Qt.AlignCenter)
        self.band_values_label.hide()

        self.graphics_view.mouseMoveEvent = self._update_coordinates
        self.update_zoom()

        _data.viewer_changed.emit()

    def _update_coordinates(self, event):
        if _data.viewer is not None and _data.viewer.array is not None:
            pos_in_scene = self.graphics_view.mapToScene(event.pos())

            if self.graphics_view.transform():
                pos_in_original = (
                    self.graphics_view.transform().inverted()[0].map(pos_in_scene)
                )

                if (
                    0 <= pos_in_original.x() < _data.viewer.width
                    and 0 <= pos_in_original.y() < _data.viewer.height
                ):
                    self.pixel_coordinates_x.setText(f"{int(pos_in_original.x())}")
                    self.pixel_coordinates_y.setText(f"{int(pos_in_original.y())}")

                    if _data.viewer.transform is not None:
                        transform = from_origin(
                            _data.viewer.transform[0],
                            _data.viewer.transform[3],
                            _data.viewer.transform[1],
                            _data.viewer.transform[5],
                        )
                        pos_transformed = transform * (
                            pos_in_scene.x(),
                            pos_in_scene.y(),
                        )

                        self.lat_coordinates_label.setText(f"{pos_transformed[0]}")
                        self.lng_coordinates_label.setText(f"{pos_transformed[1]}")
                    else:
                        self.lat_coordinates_label.setText("N/A")
                        self.lng_coordinates_label.setText("N/A")

                    self._set_pixel_values(
                        event, int(pos_in_original.x()), int(pos_in_original.y())
                    )
                    return

        self.pixel_coordinates_x.setText("N/A")
        self.pixel_coordinates_y.setText("N/A")
        self.lat_coordinates_label.setText("N/A")
        self.lng_coordinates_label.setText("N/A")

    def _pixel_values_toggle_callback(self):
        if not self.pixel_value_button.isChecked():
            self.band_values_label.hide()
        else:
            self.band_values_label.show()

    def _set_pixel_values(self, event, x, y):
        if not self.band_values_label.isHidden():
            band_values = ""
            if _data.viewer.array is not None:
                if _data.viewer.count > 1:
                    for i in range(_data.viewer.count):
                        band_values += f"{_data.viewer.array[y, x, i]} \n"
                else:
                    band_values = f"{_data.viewer.array[y, x]}"

            cursor_pos = self.graphics_view.mapToScene(event.pos())
            self.band_values_label.setText(f"{band_values}")
            self.band_values_label.move(cursor_pos.x() - 5, cursor_pos.y() - 5)

    def update_zoom(self):
        zoom_value = self.zoom_slider.value()
        self.current_zoom = 1.0 + zoom_value / 100.0
        self.graphics_view.setTransform(
            QTransform().scale(self.current_zoom, self.current_zoom)
        )
        self.zoom_value_label.setText(f"{self.current_zoom:.2f}")

    def restore_zoom(self):
        self.zoom_slider.setValue(0)
        self.update_zoom()

    def update_viewer(self):
        self.colormap_combobox.setEnabled(False)

        if _data.viewer is not None and _data.viewer.array is not None:
            self.colormap_combobox.setEnabled(
                _data.viewer.count == 1 or _data.viewer.count == 2
            )

            temp_file_path = tempfile.mktemp(
                suffix=".png", prefix="temp_image_", dir=tempfile.gettempdir()
            )

            fig, ax = plt.subplots()
            fig.patch.set_alpha(0)

            if _data.viewer.count == 2:
                normal_data = _data.viewer.array[..., 0]
                alpha_channel = np.interp(
                    _data.viewer.array[..., 1],
                    (
                        _data.viewer.array[..., 1].min(),
                        _data.viewer.array[..., 1].max(),
                    ),
                    (0, 1),
                )

                ax.imshow(
                    normal_data,
                    cmap=COLORMAPS[self.colormap_combobox.currentText()],
                    alpha=alpha_channel,
                )
            else:
                ax.imshow(
                    _data.viewer.array,
                    cmap=COLORMAPS[self.colormap_combobox.currentText()],
                )

            ax.axis("off")
            ax.set_frame_on(False)

            plt.savefig(temp_file_path, format="png", transparent=True)
            plt.close()

            image = QImage(temp_file_path)
            pixmap = QPixmap.fromImage(image)
            os.remove(temp_file_path)

            self.scene.clear()

            image_item = QGraphicsPixmapItem(pixmap)

            self.scene.addItem(image_item)

            self.update_zoom()

    def show_info(self):
        info_window = _LayerInfoWindow("Viewer Data", _data.viewer, self)
        info_window.exec_()
