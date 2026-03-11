from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_SUCCESS_POSSIBLE_WORDS,
)


class TestMessages:
    def test_success_possible_words_is_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_POSSIBLE_WORDS, str)

    def test_success_possible_words_is_not_empty(self) -> None:
        assert len(MESSAGE_SUCCESS_POSSIBLE_WORDS) > 0

    def test_success_possible_words_contains_placeholder(self) -> None:
        assert "{words}" in MESSAGE_SUCCESS_POSSIBLE_WORDS

    def test_success_possible_words_formats_correctly(self) -> None:
        result: str = MESSAGE_SUCCESS_POSSIBLE_WORDS.format(words="hello, helo")
        assert "hello, helo" in result

    def test_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_error_app_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_APP) > 0

    def test_not_valid_fields_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FIELDS, str)

    def test_not_valid_fields_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_FIELDS) > 0

    def test_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_not_found_dialog_type_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            MESSAGE_SUCCESS_POSSIBLE_WORDS,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(all_messages) == len(set(all_messages))
