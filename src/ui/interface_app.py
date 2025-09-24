from tkinter import CENTER, Button, Entry, Label, StringVar, Tk

from src.utils.helpers import check_word
from src.utils.styles import PRIMARY, ROBOTO_15, ROBOTO_20, SECONDARY, WHITE


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = SECONDARY) -> None:
        self.root = root
        self.root.title("Spelling Checker")
        self.root.geometry("1080x350")
        self.root.resizable(False, False)
        self.root.config(bg=bg)

        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.word_entry = StringVar()
        self.final_words = StringVar()

        Entry(
            width=50,
            font=(ROBOTO_20),
            textvariable=self.word_entry,
            bg=PRIMARY,
            fg=WHITE,
            border=0,
        ).place(x=540, y=100, anchor=CENTER)

        Button(
            width=10,
            text="Check",
            font=(ROBOTO_15),
            cursor="hand2",
            command=self._spell_check,
            bg=PRIMARY,
            fg=WHITE,
            border=0,
        ).place(x=540, y=180, anchor=CENTER)

        Label(
            font=(ROBOTO_15),
            textvariable=self.final_words,
            border=1,
            bg=SECONDARY,
            fg=WHITE,
        ).place(x=540, y=250, anchor=CENTER)

    def _spell_check(self) -> None:
        word = self.word_entry.get()
        result = check_word(word)

        if isinstance(result, str):
            self.final_words.set(result)
        else:
            self.final_words.set(f'Possible words: {", ".join(result)}')
