import tkinter as tk

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_instantiation(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_check=lambda: None)
        assert view is not None

    def test_is_frame(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_check=lambda: None)
        assert isinstance(view, tk.Frame)

    def test_word_entry_is_string_var(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_check=lambda: None)
        assert isinstance(view.word_entry, tk.StringVar)

    def test_word_entry_default_value(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_check=lambda: None)
        assert view.word_entry.get() == ""

    def test_set_result_updates_text(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_check=lambda: None)
        view.set_result("Possible words: hello")
        assert view._result_text.get() == "Possible words: hello"

    def test_set_result_empty_string(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_check=lambda: None)
        view.set_result("")
        assert view._result_text.get() == ""

    def test_set_result_overwrites_previous(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), on_check=lambda: None)
        view.set_result("first")
        view.set_result("second")
        assert view._result_text.get() == "second"
