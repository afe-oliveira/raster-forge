import shutil
import tempfile

import numpy as np
from matplotlib import pyplot as plt
from PySide6.QtWidgets import QFileDialog
from rforge.gui.data import _data


def _save_as_layer():
    if _data.viewer is not None and _data.raster is not None:
        _data.raster.add_layer(_data.viewer, "Layer")
    _data.raster_changed.emit()


def _save_as_geotiff():
    if _data.viewer is not None and _data.raster is not None:
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(
            None, "Save as TIFF", "", "TIFF Files (*.tif *.tiff)"
        )

        if file_path:
            tiff_data = _data.viewer.array.astype(np.uint8)
            import tifffile

            tifffile.imwrite(file_path, tiff_data)


def _save_as_image(colormap: str = "viridis"):
    if _data.viewer is not None and _data.raster is not None:
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(
            None, "Save as Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_path:
            temp_file_path = tempfile.mktemp(
                suffix=".png", prefix="temp_image_", dir=tempfile.gettempdir()
            )

            image_data = _data.viewer.array
            plt.imshow(image_data, cmap=colormap)
            plt.axis("off")
            plt.savefig(temp_file_path, format="png", transparent=True)
            plt.close()

            shutil.move(temp_file_path, file_path)
