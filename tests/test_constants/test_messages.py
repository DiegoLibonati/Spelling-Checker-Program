from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_SUCCESS_POSSIBLE_WORDS,
)


class TestMessages:
    def test_message_success_possible_words_is_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_POSSIBLE_WORDS, str)

    def test_message_success_possible_words_has_placeholder(self) -> None:
        assert "{words}" in MESSAGE_SUCCESS_POSSIBLE_WORDS

    def test_message_success_format(self) -> None:
        result: str = MESSAGE_SUCCESS_POSSIBLE_WORDS.format(words="hello, helo")
        assert "hello, helo" in result

    def test_message_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_message_not_valid_fields_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FIELDS, str)

    def test_message_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)
