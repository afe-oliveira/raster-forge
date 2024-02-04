import sys
import atexit
import gc
from PySide6.QtCore import QFile, QTextStream, QTimer, Qt
from PySide6.QtWidgets import QApplication
from .main_window import _MainWindow
from .resources import resources


def _cleanup(main_window):
    main_window.close()


atexit.register(_cleanup)


def _show_main_window(main_window):
    main_window.show()


def _initialize_application():
    app = QApplication(sys.argv)

    # Set the Style Sheet
    style_file = QFile(":/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(style_file)
    app.setStyleSheet(stream.readAll())
    style_file.close()

    return app


def gui():
    """Launches the Raster Forge Graphical User Interface (GUI)."""
    global main_window
    try:
        app = _initialize_application()
        main_window = _MainWindow()

        # Connect the Cleanup Function
        app.aboutToQuit.connect(lambda: _cleanup(main_window))

        # Delay Showing the Main Window
        delay_timer = QTimer.singleShot(1000, lambda: _show_main_window(main_window))

        sys.exit(app.exec_())

    except Exception as e:
        print(f"An Error Occurred During Initialization: {e}")
    finally:
        _cleanup(main_window)
