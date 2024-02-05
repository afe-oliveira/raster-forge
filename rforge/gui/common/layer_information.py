import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QScrollArea,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from rforge.gui.common.adaptative_elements import _adaptative_label


class _LayerInfoWindow(QDialog):
    def __init__(self, name, layer, parent=None):
        super().__init__(parent)
        self.name = name
        self.setWindowTitle(f"Layer Information - {self.name}")

        # Create a Tab Widget
        self.tab_widget = QTabWidget(self)

        # Create General Information
        general = [
            (layer.width, "Width"),
            (layer.height, "Height"),
            (layer.count, "Count"),
            None,
            (layer.driver, "Driver"),
            (layer.no_data, "No Data"),
            (layer.units, "Units"),
            None,
            (
                layer.transform,
                "Transform",
                [
                    "Top-Left X",
                    "Pixel Width",
                    "Row Rotation",
                    "Top-Left Y",
                    "Column Rotation",
                    "Pixel Height",
                ],
            ),
            None,
            (layer.crs, "CRS"),
            None,
            (
                layer.bounds,
                "Bounds",
                {"left": "Left", "right": "Right", "top": "Top", "bottom": "Bottom"},
            ),
        ]

        # Create Statistical Information
        statistics = [
            (layer.min, "Minimum"),
            (layer.max, "Maximum"),
            None,
            (layer.mean, "Mean"),
            (layer.median, "Median"),
            (layer.std_dev, "Standard Deviation"),
        ]

        # Create Information Tabs
        self._numerical_tab(general, "General")
        self._numerical_tab(statistics, "Statistics")
        self._histogram_tab(layer)

        # Set Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def _numerical_tab(self, properties, name):
        # Create a Scroll Area for General Information
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget(self)
        scroll_area.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)

        for items in properties:
            if items is None:
                # Add Separator
                separator = QFrame()
                separator.setFrameShape(QFrame.HLine)
                separator.setFrameShadow(QFrame.Sunken)
                scroll_layout.addWidget(separator)
            else:
                scroll_layout.addWidget(_adaptative_label(*items))

        scroll_content.setLayout(scroll_layout)
        self.tab_widget.addTab(scroll_area, name)

    def _histogram_tab(self, layer):
        # Clean Min and Max
        cleaned_data = layer.array.astype(float)
        cleaned_data[(cleaned_data == layer.min) | (cleaned_data == layer.max)] = np.nan

        # Create a Scroll Area for Graph
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget(self)
        scroll_area.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)

        # Create a Matplotlib Figure and Canvas
        figure, ax = plt.subplots(figsize=(5, 4), tight_layout=True)
        canvas = FigureCanvas(figure)
        scroll_layout.addWidget(canvas)

        # Calculate Histogram
        colors = [
            "#DAAC3D",
            "#D3A334",
            "#CC9A2B",
            "#C69322",
            "#BF8B19",
            "#B88410",
            "#B17C07",
            "#AA7500",
            "#A36E00",
            "#9C6700",
        ]
        if layer.count > 1:
            for band in range(layer.count):
                band_data = cleaned_data[..., band]
                valid_data = band_data[~np.isnan(band_data)].flatten()

                ax.hist(
                    valid_data,
                    bins=100,
                    color=colors[band],
                    histtype="bar",
                    label=f"Band {band + 1}",
                    density=True,
                )
                ax.legend()
        else:
            ax.hist(
                cleaned_data[~np.isnan(cleaned_data)].flatten(),
                bins=100,
                color=colors[0],
                histtype="bar",
                density=True,
            )

        ax.set_xlabel("Pixel Value")
        ax.set_ylabel("Percentage")

        # Add the Matplotlib Canvas to the Scroll Layout
        scroll_layout.addWidget(canvas)

        scroll_content.setLayout(scroll_layout)
        self.tab_widget.addTab(scroll_area, "Line Graph")
