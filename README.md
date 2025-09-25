# Spelling Checker Program

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app` to execute program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

I made a python program with a user interface made with tkinter. This program allows to correct the user through an entered word, if the user enters `hell` it will appear words similar to `hell` like `hello` for example.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
pyspellchecker==0.8.3
pre-commit==4.3.0
```

#### Requirements.test.txt

```
pytest==8.4.2
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Spelling-Checker-Program`](https://www.diegolibonati.com.ar/#/project/Spelling-Checker-Program)

## Video

https://user-images.githubusercontent.com/99032604/199130391-d38d60be-34b2-468a-8c12-ca521ac0b685.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Join to the correct path of the clone
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller --onefile --windowed --add-data "venv\Lib\site-packages\spellchecker\resources;spellchecker\resources" src/app.py`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Join to the correct path of the clone
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller --onefile --windowed --add-data "venv\Lib\site-packages\spellchecker\resources;spellchecker\resources" src/app.py`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues
