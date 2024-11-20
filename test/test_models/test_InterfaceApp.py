import logging

from textblob import Word

from src.models.InterfaceApp import InterfaceApp
from src.utils.constants import SECONDARY
from src.utils.constants import ERROR_NOT_WORD


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CUSTOM_BG = "" or SECONDARY


def test_initial_config_tk_app(interface_app: InterfaceApp) -> None:
    root = interface_app.root
    root.update()

    title = root.title
    geometry = root.geometry().split("+")[0]
    resizable = root.resizable()
    config_bg = root.cget("bg")

    assert title == "Spelling Checker"
    assert geometry == "1080x350"
    assert resizable == (False, False)
    assert config_bg == CUSTOM_BG


def test_spell_check(interface_app: InterfaceApp) -> None:
    word = "hel"
    spelling_get = Word(word).spellcheck()
    word_spelling_list = [tuple[0] for tuple in spelling_get]

    interface_app.word_entry.set(word)
    interface_app._spell_check()

    final_words = interface_app.final_words

    assert final_words.get() == f'Possible words: {", ".join(word_spelling_list)}'


def test_spell_check_without_word(interface_app: InterfaceApp) -> None:
    interface_app.word_entry.set("  ")

    interface_app._spell_check()
    final_words = interface_app.final_words

    assert final_words.get() == ERROR_NOT_WORD

def test_get_words(interface_app: InterfaceApp) -> None:
    list_tuple = [("hi", "1.0"), ("hello", "0.5")]

    list_words = interface_app._get_words(list=list_tuple)

    assert list_words == ["hi", "hello"]