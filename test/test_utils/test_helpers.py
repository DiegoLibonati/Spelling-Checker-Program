import logging

from textblob import Word

from src.utils.helpers import check_word
from src.utils.messages import MESSAGE_ERROR_NOT_WORD

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def test_check_word_valid():
    word = "hel"
    result = check_word(word)

    spelling_get = Word(word).spellcheck()
    expected = [suggestion for suggestion, _ in spelling_get]

    assert isinstance(result, list)
    assert result == expected


def test_check_word_empty_string():
    result = check_word("   ")
    assert result == MESSAGE_ERROR_NOT_WORD


def test_check_word_single_exact():
    word = "hello"
    result = check_word(word)

    assert "hello" in result
