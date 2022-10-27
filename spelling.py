from tkinter import *
from tkinter import ttk
from textblob import Word

class SpellingCheckerApp:

    def __init__(self,master):
        master.title('Spelling Checker')
        master.geometry('1080x350')
        master.config(bg='#B983FF')
        master.resizable('False', 'False')
        
        self.word_entry = StringVar()
        self.final_words = StringVar()

        Entry(width=50, font=('Roboto 20'), textvariable=self.word_entry, bg="#94B3FD", fg="#fff", border=0).place(x = 540, y = 100, anchor=CENTER)

        Button(width=10, text='Check', font=('Roboto 15'), cursor='hand2',command=lambda:self.load_values(), bg="#94B3FD", fg="#fff", border=0).place(x=540, y=180, anchor=CENTER)

        Label(font=('Roboto 15'), textvariable=self.final_words, border=1, bg="#B983FF", fg="#fff").place(x=540, y=250, anchor=CENTER)


    def load_values(self):

        word_spelling_list = []
        word = self.word_entry.get()

        spelling_get = Word(word).spellcheck()

        if word == "":
            return self.final_words.set('There are not words load')

        if len(spelling_get) > 1:
            for tupla in spelling_get:
                for word in tupla:
                    if isinstance(word, str):
                        word_spelling_list.append(word)
        else:
            return self.final_words.set(f'Possible words: {spelling_get[0][0]}')


       

        return self.final_words.set(f'Possible words: {" ".join(word_spelling_list)}')
root = Tk()

spelling_program = SpellingCheckerApp(root)

root.mainloop()