import pytest

from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_SUCCESS_POSSIBLE_WORDS,
)


class TestMessages:
    @pytest.mark.parametrize(
        "constant",
        [
            MESSAGE_SUCCESS_POSSIBLE_WORDS,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ],
    )
    def test_all_constants_are_strings(self, constant: str) -> None:
        assert isinstance(constant, str)

    def test_success_message_has_words_placeholder(self) -> None:
        assert "{words}" in MESSAGE_SUCCESS_POSSIBLE_WORDS

    def test_success_message_formats_correctly(self) -> None:
        result: str = MESSAGE_SUCCESS_POSSIBLE_WORDS.format(words="hello, helo")

        assert "hello, helo" in result
