from tkinter import Button, Entry, Frame, Misc, StringVar

from src.ui.styles import Styles


class WordInput(Frame):
    def __init__(self, parent: Misc, styles: Styles, variable: StringVar, on_check: callable) -> None:
        super().__init__(parent, bg=styles.SECONDARY_COLOR)
        self._styles = styles
        self._variable = variable
        self._on_check = on_check

        self.columnconfigure(0, weight=1)

        Entry(
            self,
            width=50,
            font=self._styles.FONT_ROBOTO_20,
            textvariable=self._variable,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
            border=0,
        ).grid(row=0, column=0, pady=(0, 20))

        Button(
            self,
            width=10,
            text="Check",
            font=self._styles.FONT_ROBOTO_15,
            cursor="hand2",
            command=self._on_check,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
            border=0,
        ).grid(row=1, column=0)
