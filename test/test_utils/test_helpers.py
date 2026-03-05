from unittest.mock import MagicMock, patch

from src.constants.messages import MESSAGE_ERROR_NOT_WORD
from src.utils.helpers import check_word


class TestCheckWord:
    def test_returns_error_message_for_empty_string(self) -> None:
        result: list[str] | str = check_word("")
        assert result == MESSAGE_ERROR_NOT_WORD

    def test_returns_error_message_for_whitespace_only(self) -> None:
        result: list[str] | str = check_word("   ")
        assert result == MESSAGE_ERROR_NOT_WORD

    def test_returns_list_for_valid_word(self) -> None:
        with patch("src.utils.helpers.SpellChecker") as mock_spell_checker_class:
            mock_spell: MagicMock = MagicMock()
            mock_spell.candidates.return_value = {"hello", "helo"}
            mock_spell_checker_class.return_value = mock_spell
            result: list[str] | str = check_word("hello")

        assert isinstance(result, list)

    def test_returns_candidates_from_spell_checker(self) -> None:
        with patch("src.utils.helpers.SpellChecker") as mock_spell_checker_class:
            mock_spell: MagicMock = MagicMock()
            mock_spell.candidates.return_value = {"hello", "helo"}
            mock_spell_checker_class.return_value = mock_spell
            result: list[str] | str = check_word("helo")

        assert isinstance(result, list)
        assert set(result) == {"hello", "helo"}

    def test_spell_checker_called_with_word(self) -> None:
        with patch("src.utils.helpers.SpellChecker") as mock_spell_checker_class:
            mock_spell: MagicMock = MagicMock()
            mock_spell.candidates.return_value = {"test"}
            mock_spell_checker_class.return_value = mock_spell
            check_word("test")

        mock_spell.candidates.assert_called_once_with("test")

    def test_returns_string_for_empty_input(self) -> None:
        result: list[str] | str = check_word("")
        assert isinstance(result, str)

    def test_word_with_leading_trailing_spaces_is_valid(self) -> None:
        with patch("src.utils.helpers.SpellChecker") as mock_spell_checker_class:
            mock_spell: MagicMock = MagicMock()
            mock_spell.candidates.return_value = {"hello"}
            mock_spell_checker_class.return_value = mock_spell
            result: list[str] | str = check_word("  hello  ")

        assert isinstance(result, list)
