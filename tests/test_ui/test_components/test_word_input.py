import tkinter as tk
from tkinter import Frame
from unittest.mock import MagicMock

import pytest

from src.ui.components.word_input import WordInput
from src.ui.styles import Styles


@pytest.mark.unit
class TestWordInput:
    def test_initializes_without_error(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar()
        callback: MagicMock = MagicMock()

        widget: WordInput = WordInput(
            parent=root, styles=styles, variable=variable, on_check=callback
        )

        assert widget is not None

    def test_is_frame_instance(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar()
        callback: MagicMock = MagicMock()

        widget: WordInput = WordInput(
            parent=root, styles=styles, variable=variable, on_check=callback
        )

        assert isinstance(widget, Frame)

    def test_background_matches_secondary_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar()
        callback: MagicMock = MagicMock()

        widget: WordInput = WordInput(
            parent=root, styles=styles, variable=variable, on_check=callback
        )

        assert widget.cget("bg") == styles.SECONDARY_COLOR

    def test_on_check_callback_is_called(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: tk.StringVar = tk.StringVar()
        callback: MagicMock = MagicMock()
        widget: WordInput = WordInput(
            parent=root, styles=styles, variable=variable, on_check=callback
        )

        widget._on_check()

        callback.assert_called_once()
