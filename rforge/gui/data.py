from PySide6.QtCore import QObject, Signal
from rforge.containers.layer import Layer
from rforge.containers.raster import Raster


class _DataGUI(QObject):

    # General Data
    raster: Raster = None
    viewer: Layer = None

    # Signals
    raster_changed = Signal()
    viewer_changed = Signal()

    process_main = Signal()

    def __init__(self):
        super().__init__()


_data = _DataGUI()
