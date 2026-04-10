import tkinter as tk

from src.ui.components.word_input import WordInput
from src.ui.styles import Styles


class TestWordInput:
    def test_instantiation(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        widget: WordInput = WordInput(
            parent=root,
            styles=Styles(),
            variable=variable,
            on_check=lambda: None,
        )
        assert widget is not None

    def test_is_frame(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        widget: WordInput = WordInput(
            parent=root,
            styles=Styles(),
            variable=variable,
            on_check=lambda: None,
        )
        assert isinstance(widget, tk.Frame)

    def test_variable_is_stored(self, root: tk.Tk) -> None:
        variable: tk.StringVar = tk.StringVar(root)
        widget: WordInput = WordInput(
            parent=root,
            styles=Styles(),
            variable=variable,
            on_check=lambda: None,
        )
        assert widget._variable is variable

    def test_on_check_callback_is_stored(self, root: tk.Tk) -> None:
        def callback() -> None:
            pass

        variable: tk.StringVar = tk.StringVar(root)
        widget: WordInput = WordInput(
            parent=root,
            styles=Styles(),
            variable=variable,
            on_check=callback,
        )
        assert widget._on_check is callback

    def test_on_check_callback_is_called(self, root: tk.Tk) -> None:
        called: list[bool] = []
        variable: tk.StringVar = tk.StringVar(root)

        def callback() -> None:
            called.append(True)

        widget: WordInput = WordInput(
            parent=root,
            styles=Styles(),
            variable=variable,
            on_check=callback,
        )
        widget._on_check()
        assert called == [True]
