from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_NOT_VALID_FIELDS
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.MainView") as mock_main_view_class:
        mock_main_view: MagicMock = MagicMock()
        mock_main_view.grid = MagicMock()
        mock_main_view_class.return_value = mock_main_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance._main_view = mock_main_view
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles == mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root == mock_root

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

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())

        assert isinstance(app._styles, Styles)

    def test_main_view_receives_on_check(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_check"))


class TestInterfaceAppSpellCheck:
    def test_validation_dialog_called_when_check_word_returns_string(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = ""

        with (
            patch("src.ui.interface_app.check_word", return_value=MESSAGE_NOT_VALID_FIELDS),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            interface_app._spell_check()

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_FIELDS)
        mock_dialog.dialog.assert_called_once()

    def test_set_result_called_when_check_word_returns_list(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "helo"

        with patch("src.ui.interface_app.check_word", return_value=["hello", "helo"]):
            interface_app._spell_check()

        interface_app._main_view.set_result.assert_called_once()

    def test_set_result_contains_words_joined(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "helo"

        with patch("src.ui.interface_app.check_word", return_value=["hello", "helo"]):
            interface_app._spell_check()

        call_arg: str = interface_app._main_view.set_result.call_args[0][0]
        assert "hello" in call_arg
        assert "helo" in call_arg

    def test_set_result_not_called_when_check_word_returns_string(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = ""

        with (
            patch("src.ui.interface_app.check_word", return_value=MESSAGE_NOT_VALID_FIELDS),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            interface_app._spell_check()

        interface_app._main_view.set_result.assert_not_called()

    def test_check_word_called_with_entry_value(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "python"

        with patch("src.ui.interface_app.check_word", return_value=["python"]) as mock_check:
            interface_app._spell_check()

        mock_check.assert_called_once_with("python")

    def test_validation_dialog_not_called_when_check_word_returns_list(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.word_entry.get.return_value = "hello"

        with (
            patch("src.ui.interface_app.check_word", return_value=["hello"]),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            interface_app._spell_check()

        mock_dialog_class.assert_not_called()
