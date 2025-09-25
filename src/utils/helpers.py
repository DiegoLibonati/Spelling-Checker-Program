from spellchecker import SpellChecker

from src.utils.messages import MESSAGE_ERROR_NOT_WORD


def check_word(word: str) -> list[str] | str:
    if not word.strip():
        return MESSAGE_ERROR_NOT_WORD

    spell = SpellChecker()

    # correction = spell.correction(word)

    suggestions = spell.candidates(word)

    return list(suggestions)
