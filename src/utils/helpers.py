from textblob import Word

from src.utils.messages import MESSAGE_ERROR_NOT_WORD


def check_word(word: str) -> list[str] | str:
    if not word.strip():
        return MESSAGE_ERROR_NOT_WORD

    spelling_get = Word(word).spellcheck()
    return [suggestion for suggestion, _ in spelling_get]
