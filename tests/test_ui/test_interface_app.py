import tkinter as tk

import pytest

from src.configs.testing_config import TestingConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


class TestInterfaceApp:
    def test_instantiation(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=TestingConfig())
        assert app is not None

    def test_title_is_set(self, root: tk.Tk) -> None:
        InterfaceApp(root=root, config=TestingConfig())
        assert root.title() == "WordSentry"

    def test_main_view_is_created(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=TestingConfig())
        assert app._main_view is not None

    def test_config_is_stored(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._config is config

    def test_styles_default(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=TestingConfig())
        assert isinstance(app._styles, Styles)

    def test_styles_custom(self, root: tk.Tk) -> None:
        custom_styles: Styles = Styles()
        app: InterfaceApp = InterfaceApp(root=root, config=TestingConfig(), styles=custom_styles)
        assert app._styles is custom_styles

    def test_spell_check_empty_word_raises(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=TestingConfig())
        app._main_view.word_entry.set("")
        with pytest.raises(ValidationDialogError):
            app._spell_check()

    def test_spell_check_blank_word_raises(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=TestingConfig())
        app._main_view.word_entry.set("   ")
        with pytest.raises(ValidationDialogError):
            app._spell_check()

    def test_spell_check_valid_word_sets_result(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=TestingConfig())
        app._main_view.word_entry.set("hello")
        app._spell_check()
        result: str = app._main_view._result_text.get()
        assert result.startswith("Possible words:")
