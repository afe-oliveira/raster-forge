import os
import tempfile

import numpy as np
from PySide6.QtWidgets import (
    QGraphicsView, QGraphicsScene, QLabel, QVBoxLayout, QHBoxLayout,
    QGraphicsPixmapItem, QWidget, QPushButton, QGridLayout, QSlider, QFrame
)
from PySide6.QtGui import QPixmap, QTransform, QImage
from PySide6.QtCore import Qt, QRectF, QPointF
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas

from ProjectNabu.gui.data import data

class ViewerPanel(QWidget):

    current_zoom = 0.5
    layer = None

    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        data.viewer_changed.connect(self.update_viewer)

        # Add Graphics Scene and Graphics View
        self.scene = QGraphicsScene(self)
        self.graphics_view = QGraphicsView(self.scene)
        self.graphics_view.setMouseTracking(True)
        layout.addWidget(self.graphics_view, 0, 0, 47, 25)

        self.graphics_view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

        # Add Zoom Slider
        self.zoom_slider = QSlider()
        self.zoom_slider.setOrientation(Qt.Horizontal)
        self.zoom_slider.setMinimum(-50)
        self.zoom_slider.setMaximum(1950)
        self.zoom_slider.setValue(-50)

        self.zoom_label = QLabel("Zoom:")
        self.zoom_value_label = QLabel("1.0")
        self.restore_zoom_button = QPushButton("Restore Zoom")

        layout.addWidget(self.zoom_label, 48, 0, 1, 1)
        layout.addWidget(self.zoom_slider, 48, 1, 1, 22)
        layout.addWidget(self.zoom_value_label, 48, 23, 1, 1)
        layout.addWidget(self.restore_zoom_button, 48, 24, 1, 1)

        self.zoom_slider.valueChanged.connect(self.update_zoom)
        self.restore_zoom_button.clicked.connect(self.restore_zoom)

        # Add a Separator
        separator_line = QFrame()
        separator_line.setFrameShape(QFrame.HLine)
        separator_line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator_line, 49, 0, 1, 25)

        # Add Coordinate Display
        self.pixel_coordinates_label = QLabel("N/A")
        layout.addWidget(self.pixel_coordinates_label, 50, 0, 1, 5)

        self.lat_lng_coordinates_label = QLabel("N/A")
        self.lat_lng_coordinates_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(self.lat_lng_coordinates_label, 50, 20, 1, 5)

        # Initialize a QLabel for displaying band values
        self.band_values_label = QLabel("", self)
        self.band_values_label.setGeometry(0, 0, 100, 50)
        self.band_values_label.setStyleSheet("background-color: rgba(255, 255, 255, 200); border: 1px solid black;")
        self.band_values_label.hide()

        self.graphics_view.mouseMoveEvent = self.update_coordinates
        self.update_zoom()

        data.viewer_changed.emit()

    def update_coordinates(self, event):
        pos_in_scene = self.graphics_view.mapToScene(event.pos())
        pixel_coordinates = f"({int(pos_in_scene.x())}, {int(pos_in_scene.y())})"
        self.pixel_coordinates_label.setText(f"{pixel_coordinates}")

        transform = None  # layer_data.transform
        if transform is not None:
            inverted_transform = transform.inverted()[0]
            pos_in_original = inverted_transform.map(pos_in_scene)

            lat_lng_coordinates = f"({pos_in_original.x()}, {pos_in_original.y()})"
            self.lat_lng_coordinates_label.setText(f"{lat_lng_coordinates}")
        else:
            self.lat_lng_coordinates_label.setText(f"N/A")

        # Show the band values popup near the mouse cursor
        band_values = self.get_band_values(pos_in_scene)
        self.show_band_values_popup(event, band_values)

    def show_band_values_popup(self, event, band_values):
        # Show the band values popup near the mouse cursor
        cursor_pos = self.graphics_view.mapToScene(event.pos())
        self.band_values_label.setText(f"Band Values: {band_values}")
        self.band_values_label.move(cursor_pos.x() + 10, cursor_pos.y() + 10)
        self.band_values_label.show()

    def get_band_values(self, pos_in_scene):
        # Replace this with your logic to get band values at the given position
        band_values = "Band 1: 100, Band 2: 150, Band 3: 200"
        return band_values

    def update_zoom(self):
        zoom_value = self.zoom_slider.value()
        self.current_zoom = 1.0 + zoom_value / 100.0
        self.graphics_view.setTransform(QTransform().scale(self.current_zoom, self.current_zoom))
        self.zoom_value_label.setText(f"{(self.current_zoom - 0.5):.2f}")

    def restore_zoom(self):
        self.zoom_slider.setValue(-50)
        self.update_zoom()

    def update_viewer(self):
        if data.viewer is not None and data.viewer.data is not None:
            temp_file_path = tempfile.mktemp(suffix=".png", prefix="temp_image_", dir=tempfile.gettempdir())

            fig, ax = plt.subplots()
            fig.patch.set_alpha(0)

            ax.imshow(data.viewer.data, cmap='gray')
            ax.axis('off')
            ax.set_frame_on(False)

            plt.savefig(temp_file_path, format='png', transparent=True)
            plt.close()

            image = QImage(temp_file_path)
            pixmap = QPixmap.fromImage(image)
            os.remove(temp_file_path)

            self.scene.clear()

            image_item = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(image_item)

            self.update_zoom()
