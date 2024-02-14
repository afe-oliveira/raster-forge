import pytest
from pytestqt.qtbot import QtBot

from rforge.gui.main_window import _MainWindow


@pytest.fixture
def main_window(qtbot: QtBot):
    main_window = _MainWindow()
    qtbot.addWidget(main_window)
    yield main_window
