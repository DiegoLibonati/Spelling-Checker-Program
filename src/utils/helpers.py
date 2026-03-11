from spellchecker import SpellChecker

from src.constants.messages import MESSAGE_NOT_VALID_FIELDS


def check_word(word: str) -> list[str] | str:
    if not word.strip():
        return MESSAGE_NOT_VALID_FIELDS

    spell = SpellChecker()

    # correction = spell.correction(word)

    suggestions = spell.candidates(word)

    return list(suggestions)
