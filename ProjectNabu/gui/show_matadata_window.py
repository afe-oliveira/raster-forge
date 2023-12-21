from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget, QVBoxLayout

class MetadataWindow(QDialog):
    def __init__(self, metadata):
        super().__init__()

        self.setWindowTitle("Metadata")

        # Create a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to contain the keys and values
        content_widget = QWidget(scroll_area)
        content_layout = QVBoxLayout(content_widget)

        # Populate the widget with keys and values
        if metadata is not None:
            for key, value in metadata.items():
                key_label = QLabel(key)
                value_label = QLabel(str(value))
                content_layout.addWidget(key_label)
                content_layout.addWidget(value_label)

        # Set the content widget for the scroll area
        scroll_area.setWidget(content_widget)

        # Create the main layout
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)