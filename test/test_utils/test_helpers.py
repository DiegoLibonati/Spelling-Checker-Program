from unittest.mock import MagicMock, patch

from src.constants.messages import MESSAGE_NOT_VALID_FIELDS
from src.utils.helpers import check_word


class TestCheckWord:
    def test_returns_not_valid_fields_when_word_is_empty(self) -> None:
        result: list[str] | str = check_word("")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_not_valid_fields_when_word_is_whitespace(self) -> None:
        result: list[str] | str = check_word("   ")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_returns_list_when_word_is_valid(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = {"hello", "helo"}
        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            result: list[str] | str = check_word("hello")
        assert isinstance(result, list)

    def test_returns_list_of_strings(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = {"hello", "helo"}
        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            result: list[str] | str = check_word("hello")
        assert all(isinstance(w, str) for w in result)

    def test_candidates_called_with_word(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = {"hello"}
        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            check_word("hello")
        mock_spell.candidates.assert_called_once_with("hello")

    def test_returns_suggestions_from_spell_checker(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = {"apple", "aple"}
        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            result: list[str] | str = check_word("aple")
        assert set(result) == {"apple", "aple"}

    def test_string_is_returned_not_set(self) -> None:
        mock_spell: MagicMock = MagicMock()
        mock_spell.candidates.return_value = {"word"}
        with patch("src.utils.helpers.SpellChecker", return_value=mock_spell):
            result: list[str] | str = check_word("word")
        assert isinstance(result, list)
        assert not isinstance(result, set)
