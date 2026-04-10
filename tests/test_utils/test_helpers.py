from src.constants.messages import MESSAGE_NOT_VALID_FIELDS
from src.utils.helpers import check_word


class TestCheckWord:
    def test_empty_string_returns_error_message(self) -> None:
        result = check_word("")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_blank_string_returns_error_message(self) -> None:
        result = check_word("   ")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_whitespace_only_returns_error_message(self) -> None:
        result = check_word("\t\n")
        assert result == MESSAGE_NOT_VALID_FIELDS

    def test_valid_word_returns_list(self) -> None:
        result = check_word("hello")
        assert isinstance(result, list)

    def test_valid_word_returns_non_empty_list(self) -> None:
        result = check_word("hello")
        assert len(result) > 0

    def test_misspelled_word_returns_list(self) -> None:
        result = check_word("helo")
        assert isinstance(result, list)

    def test_suggestions_are_strings(self) -> None:
        result = check_word("hello")
        assert all(isinstance(w, str) for w in result)
