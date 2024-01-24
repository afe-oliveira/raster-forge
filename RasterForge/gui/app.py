import os
import sys

from PySide6.QtWidgets import QApplication

from .main_window import MainWindow


def _run():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    current_module_dir = os.path.dirname(os.path.abspath(__file__))
    qss_file_path = os.path.join(current_module_dir, 'style.qss')
    with open(qss_file_path, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
