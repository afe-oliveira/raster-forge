from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLayout, QFrame, QGridLayout, \
    QScrollArea


class LayersPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        # Inner Title Panel
        layout.addWidget(QLabel("Layers"), 0, 0, 1, 8)
        layout.addWidget(QPushButton("Import Layers"), 0, 8, 1, 2)

        # Add a Separator (Horizontal Line)
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator, 1, 0, 1, 10)

        # Add Layers List
        scroll_list = QScrollArea(self)
        scroll_list.setWidgetResizable(True)

        buttons_widget = QWidget(scroll_list)
        buttons_layout = QVBoxLayout(buttons_widget)
        for i in range(20):
            button = QPushButton(f"Button {i + 1}")
            buttons_layout.addWidget(button)

        scroll_list.setWidget(buttons_widget)
        layout.addWidget(scroll_list, 2, 0, 18, 10)

class ImportLayersPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Inner Title Panel
        title_widget = QWidget()
        title_layout = QHBoxLayout(title_widget)
        title_layout.addWidget(QLabel("Layers"))
        title_layout.addWidget(QPushButton("Import Layers"))

        # Add a Separator (Horizontal Line)
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)

        layout.addWidget(title_widget)
        layout.addWidget(separator)