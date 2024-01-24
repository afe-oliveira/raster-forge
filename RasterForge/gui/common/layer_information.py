import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QLabel,
    QScrollArea,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class LayerInfoWindow(QDialog):
    def __init__(self, name, layer, parent=None):
        super().__init__(parent)
        self.name = name
        self.setWindowTitle(f"Layer Information - {self.name}")

        # Create a Tab Widget
        self.tab_widget = QTabWidget(self)

        # Create Tabs
        self.create_general_tab(layer)
        self.create_statistics_tab(layer)
        self.create_histogram_tab(layer)

        # Set the Layout for the Dialog
        layout = QVBoxLayout(self)
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def create_general_tab(self, layer):
        # Create a Scroll Area for General Information
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget(self)
        scroll_area.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)

        # Add Labels for General Information
        properties = [
            ("Driver", layer.driver),
            ("No Data", layer.no_data),
            ("Units", layer.units),
            ("Separator", None),
            ("Transform", layer.transform),
            ("CRS", layer.crs),
            ("Bounds", layer.bounds),
            ("Separator", None),
            ("Width", layer.width),
            ("Height", layer.height),
            ("Count", layer.count),
        ]

        for property_name, value in properties:
            if value is not None:
                if property_name == "Separator":
                    # Create Separator
                    separator = QFrame(self)
                    separator.setFrameShape(QFrame.HLine)
                    separator.setFrameShadow(QFrame.Sunken)
                    scroll_layout.addWidget(separator)
                elif property_name == "Transform":
                    transform_elements = [
                        ("Upper Left Corner X Coordinate", value[0]),
                        ("Pixel Width", value[1]),
                        ("Row Rotation", value[2]),
                        ("Upper Left Corner Y Coordinate", value[3]),
                        ("Column Rotation", value[4]),
                        ("Pixel Height", value[5])
                    ]
                    label = QLabel(f"{property_name}:")
                    scroll_layout.addWidget(label)
                    for element_name, element_value in transform_elements:
                        label = QLabel(f"   {element_name}: {element_value}")
                        scroll_layout.addWidget(label)
                elif property_name == "Bounds":
                    label = QLabel(f"{property_name}:")
                    for element_name, element_value in value.items():
                        label = QLabel(f"   {element_name}: {element_value}")
                        scroll_layout.addWidget(label)
                    scroll_layout.addWidget(label)
                else:
                    label = QLabel(f"{property_name}: {value}")
                    scroll_layout.addWidget(label)
            else:
                label = QLabel(f"{property_name}: N/A")
                scroll_layout.addWidget(label)

        scroll_content.setLayout(scroll_layout)
        self.tab_widget.addTab(scroll_area, "General")

    def create_statistics_tab(self, layer):
        # Create a Scroll Area for Statistical Information
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget(self)
        scroll_area.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)

        # Add Labels for Statistical Information
        properties = [
            ("Mean", layer.mean),
            ("Median", layer.median),
            ("Minimum", layer.min),
            ("Maximum", layer.max),
            ("Standard Deviation", layer.std_dev)
        ]

        for property_name, value in properties:
            label_text = f"{property_name}: {value}" if value is not None else f"{property_name}: N/A"
            label = QLabel(label_text)
            scroll_layout.addWidget(label)

        scroll_content.setLayout(scroll_layout)
        self.tab_widget.addTab(scroll_area, "Statistics")

    def create_histogram_tab(self, layer):
        # Create a Scroll Area for Histogram
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget(self)
        scroll_area.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)

        # Create a Matplotlib figure and canvas
        figure, ax = plt.subplots(figsize=(5, 4), tight_layout=True)
        canvas = FigureCanvas(figure)
        scroll_layout.addWidget(canvas)

        # Plot the histogram using layer.array data
        ax.hist(layer.array.flatten(), bins=50, color='blue', alpha=0.7)
        ax.set_title('Histogram')
        ax.set_xlabel('Pixel Values')
        ax.set_ylabel('Frequency')

        # Add the Matplotlib canvas to the scroll layout
        scroll_layout.addWidget(canvas)

        scroll_content.setLayout(scroll_layout)
        self.tab_widget.addTab(scroll_area, "Histogram")

