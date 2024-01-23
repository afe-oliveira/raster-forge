import numpy as np
from PySide6.QtCore import QObject, Signal

from RasterForge.containers.layer import Layer
from RasterForge.containers.raster import Raster


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
