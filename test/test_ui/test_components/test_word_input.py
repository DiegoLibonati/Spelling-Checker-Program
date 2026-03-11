from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.word_input import WordInput


@pytest.fixture
def word_input(mock_styles: MagicMock, variable: MagicMock, mock_on_check: MagicMock) -> WordInput:
    with (
        patch("src.ui.components.word_input.Frame.__init__", return_value=None),
        patch("src.ui.components.word_input.Entry"),
        patch("src.ui.components.word_input.Button"),
        patch.object(WordInput, "columnconfigure"),
    ):
        instance: WordInput = WordInput.__new__(WordInput)
        instance._styles = mock_styles
        instance._variable = variable
        instance._on_check = mock_on_check
        return instance


class TestWordInputInit:
    def test_stores_styles(self, word_input: WordInput, mock_styles: MagicMock) -> None:
        assert word_input._styles == mock_styles

    def test_stores_variable(self, word_input: WordInput, variable: MagicMock) -> None:
        assert word_input._variable == variable

    def test_stores_on_check(self, word_input: WordInput, mock_on_check: MagicMock) -> None:
        assert word_input._on_check == mock_on_check

    def test_entry_is_created_with_variable(self, mock_styles: MagicMock, variable: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.components.word_input.Frame.__init__", return_value=None),
            patch("src.ui.components.word_input.Entry") as mock_entry,
            patch("src.ui.components.word_input.Button") as mock_button,
            patch.object(WordInput, "columnconfigure"),
        ):
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: WordInput = WordInput.__new__(WordInput)
            instance._styles = mock_styles
            WordInput.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                variable=variable,
                on_check=mock_on_check,
            )

        _, kwargs = mock_entry.call_args
        assert kwargs.get("textvariable") == variable

    def test_button_command_is_on_check(self, mock_styles: MagicMock, variable: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.components.word_input.Frame.__init__", return_value=None),
            patch("src.ui.components.word_input.Entry") as mock_entry,
            patch("src.ui.components.word_input.Button") as mock_button,
            patch.object(WordInput, "columnconfigure"),
        ):
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: WordInput = WordInput.__new__(WordInput)
            instance._styles = mock_styles
            WordInput.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                variable=variable,
                on_check=mock_on_check,
            )

        _, kwargs = mock_button.call_args
        assert kwargs.get("command") == mock_on_check

    def test_button_text_is_check(self, mock_styles: MagicMock, variable: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.components.word_input.Frame.__init__", return_value=None),
            patch("src.ui.components.word_input.Entry") as mock_entry,
            patch("src.ui.components.word_input.Button") as mock_button,
            patch.object(WordInput, "columnconfigure"),
        ):
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: WordInput = WordInput.__new__(WordInput)
            instance._styles = mock_styles
            WordInput.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                variable=variable,
                on_check=mock_on_check,
            )

        _, kwargs = mock_button.call_args
        assert kwargs.get("text") == "Check"

    def test_columnconfigure_is_called(self, mock_styles: MagicMock, variable: MagicMock, mock_on_check: MagicMock) -> None:
        with (
            patch("src.ui.components.word_input.Frame.__init__", return_value=None),
            patch("src.ui.components.word_input.Entry") as mock_entry,
            patch("src.ui.components.word_input.Button") as mock_button,
            patch.object(WordInput, "columnconfigure") as mock_columnconfigure,
        ):
            mock_entry.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: WordInput = WordInput.__new__(WordInput)
            instance._styles = mock_styles
            WordInput.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                variable=variable,
                on_check=mock_on_check,
            )

        mock_columnconfigure.assert_called_once_with(0, weight=1)
