import sys

try:
    from PySide6.QtCore import QFile, QTextStream, QTimer
    from PySide6.QtWidgets import QApplication

    from .main_window import _MainWindow
    from .resources import resources

    GUI_COMPONENT = True
except ImportError:
    GUI_COMPONENT = False


def _cleanup(main_window):
    main_window.close()


def _show_main_window(main_window):
    main_window.show()


def _initialize_application():
    app = QApplication()

    # Set the Style Sheet
    style_file = QFile(":/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(style_file)
    app.setStyleSheet(stream.readAll())
    style_file.close()

    return app


def gui():
    """Launches the Raster Forge Graphical User Interface (GUI)."""
    if GUI_COMPONENT:
        global main_window
        try:
            app = _initialize_application()
            main_window = _MainWindow()

            # Connect the Cleanup Function
            app.aboutToQuit.connect(lambda: _cleanup(main_window))

            # Delay Showing the Main Window
            QTimer.singleShot(1000, lambda: _show_main_window(main_window))

            sys.exit(app.exec_())

        except Exception as e:
            print(f"An Error Occurred During Initialization: {e}")
        finally:
            _cleanup(main_window)
    else:
        print("ERROR: GUI COMPONENT NOT INSTALLED")
