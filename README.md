# Spelling-Checker-Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Install requirements.txt
4. Use `python spelling.py` to execute program

## Description

I made a python program with a user interface made with tkinter. This program allows to correct the user through an entered word, if the user enters `hell` it will appear words similar to `hell` like `hello` for example.

## Technologies used

1. Python

## Libraries used

1. Tkinter
2. textblob

## Galery

![Spelling-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/spellingchecker-0.jpg)

![Spelling-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/spellingchecker-1.jpg)

![Spelling-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/spellingchecker-2.jpg)

![Spelling-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/spellingchecker-3.jpg)

![Spelling-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/spellingchecker-4.jpg)

## Portfolio Link

`https://diegolibonati.github.io/DiegoLibonatiWeb/#/projects?q=Spelling%20Checker%20Program`

## Video

https://user-images.githubusercontent.com/99032604/199130391-d38d60be-34b2-468a-8c12-ca521ac0b685.mp4

## Documentation

The `load_values()` method will have the variables `word_spelling_list` which will be a list where the possible words that the user referred to are stored, `word` will be the variable in which the content of the word that the user typed is obtained and `spelling_get` will be a list in which all possible words will be stored as a tuple:

```
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
```
