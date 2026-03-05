from tkinter import Frame, Label, StringVar, Tk

from src.ui.components.word_input import WordInput
from src.ui.styles import Styles


class MainView(Frame):
    def __init__(self, root: Tk, styles: Styles, on_check: callable) -> None:
        super().__init__(root, bg=styles.SECONDARY_COLOR)
        self._styles = styles
        self._on_check = on_check

        self.word_entry = StringVar()
        self._result_text = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.columnconfigure(0, weight=1)

        WordInput(
            parent=self,
            styles=self._styles,
            variable=self.word_entry,
            on_check=self._on_check,
        ).grid(row=0, column=0, pady=(80, 20))

        Label(
            self,
            font=self._styles.FONT_ROBOTO_15,
            textvariable=self._result_text,
            border=1,
            bg=self._styles.SECONDARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=1, column=0, pady=20)

    def set_result(self, text: str) -> None:
        self._result_text.set(text)
