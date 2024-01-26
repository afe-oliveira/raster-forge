import sys

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QApplication

from .main_window import _MainWindow

from .resources import resources

def gui():
    """Launches the Raster Forge Graphical User Interface (GUI).
    """
    app = QApplication(sys.argv)
    main_window = _MainWindow()
    main_window.show()

    # Set the Style Sheet
    style_file = QFile(":/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(style_file)
    app.setStyleSheet(stream.readAll())
    style_file.close()

    sys.exit(app.exec())
