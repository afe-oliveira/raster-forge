import numpy as np
from PySide6.QtCore import Signal, QObject

from RasterForge.container.layer import Layer
from RasterForge.container.raster import Raster

class DataGUI(QObject):

    # General Data
    raster: Raster = None
    viewer: Layer = None

    # Signals
    raster_changed = Signal()
    viewer_changed = Signal()

    process_main = Signal()

    def __init__(self):
        super().__init__()


data = DataGUI()
