import os
import sys

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QApplication

from .main_window import MainWindow

from .resources import resources


def gui():
    """Launches the Raster Forge Graphical User Interface (GUI).
    """
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    style_file = QFile(":/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(style_file)
    app.setStyleSheet(stream.readAll())
    style_file.close()

    sys.exit(app.exec())
