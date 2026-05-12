import tkinter as tk
from unittest.mock import patch

import pytest

from src.configs.default_config import DefaultConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.mark.unit
class TestInterfaceApp:
    def test_initializes_without_error(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()

        app: InterfaceApp = InterfaceApp(root=root, config=config)

        assert app is not None

    def test_title_is_set_to_word_sentry(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()

        InterfaceApp(root=root, config=config)

        assert root.title() == "Word Sentry"

    def test_uses_provided_styles(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        styles: Styles = Styles()

        app: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)

        assert app._styles is styles

    def test_creates_default_styles_when_none_provided(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()

        app: InterfaceApp = InterfaceApp(root=root, config=config)

        assert isinstance(app._styles, Styles)

    def test_spell_check_raises_validation_error_for_empty_word(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.word_entry.set("")

        with pytest.raises(ValidationDialogError):
            app._spell_check()

    def test_spell_check_raises_validation_error_for_whitespace_word(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.word_entry.set("   ")

        with pytest.raises(ValidationDialogError):
            app._spell_check()

    def test_spell_check_sets_result_for_valid_word(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.word_entry.set("hello")

        with patch("src.ui.interface_app.check_word", return_value=["hello", "helo"]):
            app._spell_check()

        assert "hello" in app._main_view._result_text.get()
