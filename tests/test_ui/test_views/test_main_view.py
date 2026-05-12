import tkinter as tk
from tkinter import Frame, StringVar
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


@pytest.mark.unit
class TestMainView:
    def test_initializes_without_error(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        callback: MagicMock = MagicMock()

        view: MainView = MainView(root=root, styles=styles, on_check=callback)

        assert view is not None

    def test_is_frame_instance(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        callback: MagicMock = MagicMock()

        view: MainView = MainView(root=root, styles=styles, on_check=callback)

        assert isinstance(view, Frame)

    def test_word_entry_is_string_var(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        callback: MagicMock = MagicMock()

        view: MainView = MainView(root=root, styles=styles, on_check=callback)

        assert isinstance(view.word_entry, StringVar)

    def test_set_result_updates_result_text(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        callback: MagicMock = MagicMock()
        view: MainView = MainView(root=root, styles=styles, on_check=callback)

        view.set_result("possible words: hello")

        assert view._result_text.get() == "possible words: hello"

    def test_set_result_with_empty_string(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        callback: MagicMock = MagicMock()
        view: MainView = MainView(root=root, styles=styles, on_check=callback)

        view.set_result("")

        assert view._result_text.get() == ""
