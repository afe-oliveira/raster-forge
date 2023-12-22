from PySide6.QtWidgets import (
    QGraphicsView, QGraphicsScene, QLabel, QVBoxLayout, QHBoxLayout,
    QGraphicsPixmapItem, QWidget, QPushButton, QGridLayout, QSlider, QFrame
)
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt, QRectF, QPointF

from ProjectNabu.gui.data import layer_data

class ViewerPanel(QWidget):

    current_zoom = 1.0

    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        # Add Graphics Scene and Graphics View
        scene = QGraphicsScene(self)
        self.graphics_view = QGraphicsView(scene)
        self.graphics_view.setMouseTracking(True)
        layout.addWidget(self.graphics_view, 0, 0, 47, 25)

        self.graphics_view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

        # Load Test Image
        image_path = 'C:\\Users\\afeol\Documents\PyCharm Projects\Software RS23\local_in\mario.png'
        pixmap = QPixmap(image_path)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        # Add Zoom Slider
        self.zoom_slider = QSlider()
        self.zoom_slider.setOrientation(Qt.Horizontal)
        self.zoom_slider.setMinimum(-100)
        self.zoom_slider.setMaximum(2000)
        self.zoom_slider.setValue(0)

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

        self.graphics_view.mouseMoveEvent = self.update_coordinates

    def update_coordinates(self, event):
        pos_in_scene = self.graphics_view.mapToScene(event.pos())
        pixel_coordinates = f"({int(pos_in_scene.x())}, {int(pos_in_scene.y())})"
        self.pixel_coordinates_label.setText(f"{pixel_coordinates}")

        transform = layer_data.transform
        if transform is not None:
            inverted_transform = transform.inverted()[0]
            pos_in_original = inverted_transform.map(pos_in_scene)

            lat_lng_coordinates = f"({pos_in_original.x()}, {pos_in_original.y()})"
            self.lat_lng_coordinates_label.setText(f"{lat_lng_coordinates}")
        else:
            self.lat_lng_coordinates_label.setText(f"N/A")

    def update_zoom(self):
        zoom_value = self.zoom_slider.value()
        self.current_zoom = 1.0 + zoom_value / 100.0
        self.graphics_view.setTransform(QTransform().scale(self.current_zoom, self.current_zoom))
        self.zoom_value_label.setText(f"{self.current_zoom:.2f}")

    def restore_zoom(self):
        self.zoom_slider.setValue(0)
        self.update_zoom()