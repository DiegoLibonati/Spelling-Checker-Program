import pytest

from src.constants.messages import MESSAGE_NOT_VALID_FIELDS
from src.utils.helpers import check_word


class TestCheckWord:
    @pytest.mark.parametrize("word", ["", "   ", "\t\n"])
    def test_invalid_input_returns_error_message(self, word: str) -> None:
        result: list[str] | str = check_word(word)

        assert result == MESSAGE_NOT_VALID_FIELDS

    @pytest.mark.parametrize("word", ["hello", "helo"])
    def test_word_returns_non_empty_candidate_list(self, word: str) -> None:
        result: list[str] | str = check_word(word)

        assert isinstance(result, list)
        assert len(result) > 0
        assert all(isinstance(w, str) for w in result)
