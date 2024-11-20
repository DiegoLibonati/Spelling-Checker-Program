from tkinter import Tk
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import CENTER

from textblob import Word

from src.utils.constants import ROBOTO_15
from src.utils.constants import ROBOTO_20
from src.utils.constants import WHITE
from src.utils.constants import PRIMARY
from src.utils.constants import SECONDARY
from src.utils.constants import ERROR_NOT_WORD


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = SECONDARY) -> None:
        self.root = root
        self.root.title = "Spelling Checker"
        self.root.geometry('1080x350')
        self.root.resizable(False, False)
        self.root.config(bg=bg)

        self.__create_widgets()
        
    def __create_widgets(self) -> None:
        self.word_entry = StringVar()
        self.final_words = StringVar()

        Entry(width=50, font=(ROBOTO_20), textvariable=self.word_entry, bg=PRIMARY, fg=WHITE, border=0).place(x = 540, y = 100, anchor=CENTER)
        Button(width=10, text='Check', font=(ROBOTO_15), cursor='hand2',command=lambda:self._spell_check(), bg=PRIMARY, fg=WHITE, border=0).place(x=540, y=180, anchor=CENTER)
        Label(font=(ROBOTO_15), textvariable=self.final_words, border=1, bg=SECONDARY, fg=WHITE).place(x=540, y=250, anchor=CENTER)

    def _spell_check(self) -> None:
        word = self.word_entry.get()

        if not word.strip():
            return self.final_words.set(ERROR_NOT_WORD)
        
        spelling_get = Word(word).spellcheck()

        word_spelling_list = self._get_words(spelling_get)
                        
        return self.final_words.set(f'Possible words: {", ".join(word_spelling_list)}')
    
    @staticmethod
    def _get_words(list: list[tuple]) -> list[str]:
        return [tuple[0] for tuple in list]