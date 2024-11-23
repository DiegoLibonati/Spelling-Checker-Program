# Spelling Checker Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app` to execute program

## Description

I made a python program with a user interface made with tkinter. This program allows to correct the user through an entered word, if the user enters `hell` it will appear words similar to `hell` like `hello` for example.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
textblob==0.17.1
```

#### Requirements.test.txt

```
pytest
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Spelling-Checker-Program`](https://www.diegolibonati.com.ar/#/project/Spelling-Checker-Program)

## Video

https://user-images.githubusercontent.com/99032604/199130391-d38d60be-34b2-468a-8c12-ca521ac0b685.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`