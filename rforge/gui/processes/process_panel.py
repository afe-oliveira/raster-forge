from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QCompleter,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from rforge.gui.data import _data


class _ProcessPanel(QWidget):

    _widgets = {}
    _references = {}

    def __init__(self, name=None, selector=False, parent=None):
        super().__init__(parent)

        # Main Process Panel
        main_process_layout = QVBoxLayout(self)
        main_process_layout.setAlignment(Qt.AlignTop)

        # Inner Title Panel Label
        if name is not None:
            title_label = QLabel(name)
            title_label.setObjectName("title-label")
            main_process_layout.addWidget(title_label)

        if selector:
            self.selector_combo = QComboBox(self)
            self.selector_combo.currentIndexChanged.connect(
                self._scroll_content_callback
            )
            self.selector_combo.setEditable(True)
            self.selector_combo.setInsertPolicy(QComboBox.NoInsert)

            line_edit = self.selector_combo.lineEdit()
            line_edit.setPlaceholderText("Search...")

            completer = QCompleter(self._widgets.keys(), self)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            self.selector_combo.setCompleter(completer)

            main_process_layout.addWidget(self.selector_combo)
        else:
            self.selector_combo = None

        _data.raster_changed.connect(self._scroll_content_callback)

        # Create Scroll Area
        self.scroll_area = QScrollArea(self)
        main_process_layout.addWidget(self.scroll_area)

        content_widget = QWidget(self)
        self.scroll_layout = QVBoxLayout(content_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        content_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(content_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll-list")

        # Bottom Row Control
        bottom_layout = QHBoxLayout()

        # Add Back Button
        back_button = QPushButton("BACK")
        back_button.setObjectName("push-button-text")
        back_button.clicked.connect(self._back_callback)
        bottom_layout.addWidget(back_button)

        # Add Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(True)
        bottom_layout.addWidget(self.progress_bar)

        # Add Import Button
        build_button = QPushButton("BUILD")
        build_button.setObjectName("push-button-text")
        build_button.clicked.connect(self._build_callback)
        bottom_layout.addWidget(build_button)

        main_process_layout.addLayout(bottom_layout)

    def _scroll_content_callback(self):
        while self.scroll_layout.count() > 0:
            widget_item = self.scroll_layout.takeAt(0)
            if widget_item:
                widget = widget_item.widget()
                if widget:
                    widget.setParent(None)

        if self._widgets:
            for component, widget in self._widgets.items():
                self.scroll_layout.addWidget(widget)

    def _back_callback(self):
        _data.process_main.emit()

    def _build_callback(self):
        pass
