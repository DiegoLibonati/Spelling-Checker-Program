from tkinter import Tk

from src.configs.default_config import DefaultConfig
from src.constants.messages import MESSAGE_SUCCESS_POSSIBLE_WORDS
from src.ui.styles import Styles
from src.ui.views.main_view import MainView
from src.utils.dialogs import ValidationDialogError
from src.utils.helpers import check_word


class InterfaceApp:
    def __init__(self, root: Tk, config: DefaultConfig, styles: Styles = Styles()) -> None:
        self._styles = styles
        self._config = config
        self._root = root
        self._root.title("Spelling Checker")
        self._root.geometry("1080x350")
        self._root.resizable(False, False)
        self._root.config(background=self._styles.SECONDARY_COLOR)

        self._main_view = MainView(
            root=self._root,
            styles=self._styles,
            on_check=self._spell_check,
        )
        self._main_view.grid(row=0, column=0, sticky="nsew")

        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

    def _spell_check(self) -> None:
        word = self._main_view.word_entry.get()
        result = check_word(word)

        if isinstance(result, str):
            raise ValidationDialogError(message=result)

        self._main_view.set_result(MESSAGE_SUCCESS_POSSIBLE_WORDS.format(words=", ".join(result)))
