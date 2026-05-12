import pytest

from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_SUCCESS_POSSIBLE_WORDS,
)


@pytest.mark.unit
class TestMessages:
    def test_message_success_possible_words_contains_words_placeholder(self) -> None:
        assert "{words}" in MESSAGE_SUCCESS_POSSIBLE_WORDS

    def test_message_success_formats_with_words(self) -> None:
        result: str = MESSAGE_SUCCESS_POSSIBLE_WORDS.format(words="hello, world")

        assert "hello, world" in result

    def test_message_error_app_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)
        assert len(MESSAGE_ERROR_APP) > 0

    def test_message_not_valid_fields_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FIELDS, str)
        assert len(MESSAGE_NOT_VALID_FIELDS) > 0

    def test_message_not_found_dialog_type_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0
