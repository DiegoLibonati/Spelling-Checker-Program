from src.constants.messages import MESSAGE_ERROR_NOT_WORD


class TestMessages:
    def test_message_error_not_word_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_NOT_WORD, str)

    def test_message_error_not_word_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_NOT_WORD) > 0
