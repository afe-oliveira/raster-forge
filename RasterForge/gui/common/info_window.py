from PySide6.QtWidgets import QDialog, QScrollArea, QWidget, QVBoxLayout, QFrame, QLabel
from PySide6.QtCore import Qt

class LayerInfoWindow(QDialog):
    def __init__(self, name, layer, parent=None):
        super().__init__(parent)
        self.name = name
        self.setWindowTitle(f"Layer Information - {self.name}")

        # Create a Scroll Area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget(self)
        self.scroll_area.setWidget(self.scroll_content)

        # Create a Layout for the Scroll Content
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        # Create Labels for Properties
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
            ("Separator", None),
            ("Mean", layer.mean),
            ("Median", layer.median),
            ("Minimum", layer.min),
            ("Maximum", layer.max),
            ("Standard Deviation", layer.std_dev),
        ]

        # Add Labels to the Layout
        for property_name, value in properties:
            if value is not None:
                if property_name == "Separator":
                    # Create Separator
                    separator = QFrame(self)
                    separator.setFrameShape(QFrame.HLine)
                    separator.setFrameShadow(QFrame.Sunken)
                    self.scroll_layout.addWidget(separator)
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
                    self.scroll_layout.addWidget(label)
                    for element_name, element_value in transform_elements:
                        label = QLabel(f"   {element_name}: {element_value}")
                        self.scroll_layout.addWidget(label)
                elif property_name == "Bounds":
                    label = QLabel(f"{property_name}:")
                    for element_name, element_value in value.items():
                        label = QLabel(f"   {element_name}: {element_value}")
                        self.scroll_layout.addWidget(label)
                    self.scroll_layout.addWidget(label)
                else:
                    label = QLabel(f"{property_name}: {value}")
                    self.scroll_layout.addWidget(label)
            else:
                label = QLabel(f"{property_name}: N/A")
                self.scroll_layout.addWidget(label)
        # Set the Layout for the Dialog
        self.setLayout(self.scroll_layout)

