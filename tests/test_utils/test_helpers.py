from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_NOT_VALID_FIELDS
from src.utils.helpers import check_word


@pytest.mark.unit
class TestCheckWord:
    def test_empty_string_returns_not_valid_message(self) -> None:
        result: list[str] | str = check_word("")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_whitespace_only_returns_not_valid_message(self) -> None:
        result: list[str] | str = check_word("   ")

        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_valid_word_returns_list(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = {"hello"}

        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            result: list[str] | str = check_word("hello")

        assert isinstance(result, list)

    def test_valid_word_returns_candidates_as_list(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = {"hello", "helo"}

        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            result: list[str] | str = check_word("helo")

        assert isinstance(result, list)
        assert "hello" in result

    def test_spell_checker_candidates_is_called_with_word(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = set()

        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            check_word("test")

        mock_spell.candidates.assert_called_once_with("test")

    def test_returns_empty_list_when_no_candidates(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = set()

        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            result: list[str] | str = check_word("xyzxyz")

        assert result == []
