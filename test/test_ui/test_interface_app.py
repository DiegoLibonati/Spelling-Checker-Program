from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_SUCCESS_POSSIBLE_WORDS
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.MainView") as mock_main_view_class:
        mock_main_view_class.return_value = MagicMock()
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._config = MagicMock()
        instance._root = mock_root
        instance._main_view = mock_main_view_class.return_value
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._styles is mock_styles

    def test_stores_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._root is mock_root

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.title.assert_called_once_with("Spelling Checker")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.geometry.assert_called_once_with("1080x350")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.resizable.assert_called_once_with(False, False)

    def test_background_uses_secondary_color(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.config.assert_called_once_with(background=mock_styles.SECONDARY_COLOR)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())
        assert isinstance(app._styles, Styles)

    def test_columnconfigure_called_on_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.columnconfigure.assert_called_once_with(0, weight=1)

    def test_rowconfigure_called_on_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.rowconfigure.assert_called_once_with(0, weight=1)

    def test_main_view_receives_on_check(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_check"))

    def test_main_view_grid_called(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view: MagicMock = MagicMock()
            mock_main_view_class.return_value = mock_main_view
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_main_view.grid.assert_called_once_with(row=0, column=0, sticky="nsew")


class TestInterfaceAppSpellCheck:
    def test_raises_validation_error_when_check_word_returns_str(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "   "

        with (
            patch("src.ui.interface_app.check_word", return_value="error message"),
            pytest.raises(ValidationDialogError) as exc_info,
        ):
            interface_app._spell_check()

        assert exc_info.value.message == "error message"

    def test_set_result_called_with_formatted_words(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "colour"

        with patch("src.ui.interface_app.check_word", return_value=["color", "colour"]):
            interface_app._spell_check()

        call_args = interface_app._main_view.set_result.call_args[0][0]
        assert call_args == MESSAGE_SUCCESS_POSSIBLE_WORDS.format(words="color, colour")

    def test_set_result_not_called_when_check_word_returns_str(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = ""

        with (
            patch("src.ui.interface_app.check_word", return_value="error message"),
            pytest.raises(ValidationDialogError),
        ):
            interface_app._spell_check()

        interface_app._main_view.set_result.assert_not_called()

    def test_check_word_called_with_entry_value(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "speling"

        with patch("src.ui.interface_app.check_word", return_value=["spelling"]) as mock_check:
            interface_app._spell_check()

        mock_check.assert_called_once_with("speling")

    def test_set_result_joins_words_with_comma_and_space(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "helo"
        words: list[str] = ["hello", "help", "held"]

        with patch("src.ui.interface_app.check_word", return_value=words):
            interface_app._spell_check()

        call_args = interface_app._main_view.set_result.call_args[0][0]
        assert "hello, help, held" in call_args
