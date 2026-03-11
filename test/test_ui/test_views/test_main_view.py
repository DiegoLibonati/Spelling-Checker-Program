from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(mock_root: MagicMock, mock_styles: MagicMock, mock_on_check: MagicMock) -> MainView:
    with (
        patch("src.ui.views.main_view.Frame.__init__", return_value=None),
        patch("src.ui.views.main_view.WordInput"),
        patch("src.ui.views.main_view.Label"),
        patch("src.ui.views.main_view.StringVar"),
        patch.object(MainView, "columnconfigure"),
    ):
        instance: MainView = MainView.__new__(MainView)
        instance._styles = mock_styles
        instance._on_check = mock_on_check
        instance._result_text = MagicMock(spec=StringVar)
        instance.word_entry = MagicMock(spec=StringVar)
        return instance


class TestMainViewInit:
    def test_stores_styles(self, main_view: MainView, mock_styles: MagicMock) -> None:
        assert main_view._styles == mock_styles

    def test_stores_on_check(self, main_view: MainView, mock_on_check: MagicMock) -> None:
        assert main_view._on_check == mock_on_check

    def test_string_vars_are_created(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.WordInput") as mock_word_input,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar") as mock_string_var,
            patch.object(MainView, "columnconfigure"),
        ):
            mock_word_input.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_check=mock_on_check)

        assert mock_string_var.call_count == 2

    def test_word_input_is_created(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.WordInput") as mock_word_input,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_word_input.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_check=mock_on_check)

        mock_word_input.assert_called_once()

    def test_word_input_receives_on_check(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.WordInput") as mock_word_input,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_word_input.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_check=mock_on_check)

        _, kwargs = mock_word_input.call_args
        assert kwargs.get("on_check") == mock_on_check

    def test_word_input_receives_styles(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.WordInput") as mock_word_input,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_word_input.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_check=mock_on_check)

        _, kwargs = mock_word_input.call_args
        assert kwargs.get("styles") == mock_styles

    def test_label_is_created(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.WordInput") as mock_word_input,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_word_input.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_check=mock_on_check)

        mock_label.assert_called_once()

    def test_columnconfigure_is_called(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.WordInput") as mock_word_input,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure") as mock_columnconfigure,
        ):
            mock_word_input.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, on_check=mock_on_check)

        mock_columnconfigure.assert_called_once_with(0, weight=1)


class TestMainViewSetResult:
    def test_set_result_updates_result_text(self, main_view: MainView) -> None:
        main_view.set_result("Possible words: hello")
        main_view._result_text.set.assert_called_once_with("Possible words: hello")

    def test_set_result_with_empty_string(self, main_view: MainView) -> None:
        main_view.set_result("")
        main_view._result_text.set.assert_called_once_with("")

    def test_set_result_with_error_message(self, main_view: MainView) -> None:
        main_view.set_result("There are not words load.")
        main_view._result_text.set.assert_called_once_with("There are not words load.")
