from tkinter import StringVar
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles


@pytest.fixture
def mock_root() -> MagicMock:
    root: MagicMock = MagicMock()
    root.title = MagicMock()
    root.geometry = MagicMock()
    root.resizable = MagicMock()
    root.config = MagicMock()
    root.columnconfigure = MagicMock()
    root.rowconfigure = MagicMock()
    return root


@pytest.fixture
def mock_styles() -> MagicMock:
    styles: MagicMock = MagicMock()
    styles.PRIMARY_COLOR = "#94B3FD"
    styles.SECONDARY_COLOR = "#B983FF"
    styles.WHITE_COLOR = "#FFFFFF"
    styles.BLACK_COLOR = "#000000"
    styles.FONT_ROBOTO_12 = "Roboto 12"
    styles.FONT_ROBOTO_15 = "Roboto 15"
    styles.FONT_ROBOTO_20 = "Roboto 20"
    return styles


@pytest.fixture
def real_styles() -> Styles:
    return Styles()


@pytest.fixture
def mock_on_check() -> MagicMock:
    return MagicMock()


@pytest.fixture
def variable() -> MagicMock:
    return MagicMock(spec=StringVar)
