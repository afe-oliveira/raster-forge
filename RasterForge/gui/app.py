import sys

from PySide6.QtWidgets import QApplication

from .main_window import MainWindow


def run():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
