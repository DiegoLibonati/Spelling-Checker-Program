# WordSentry

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

**WordSentry** is a desktop application built with Python and Tkinter that helps users identify and correct spelling mistakes in real time. The application provides a clean and minimal graphical interface where the user types a word into an input field and, upon clicking the check button, receives a list of spelling suggestions powered by the `pyspellchecker` library.

The core use case is straightforward: if you are unsure whether a word is spelled correctly, you type it in and the application returns the closest matching words from its dictionary. For example, typing `recieve` will return suggestions like `receive`, helping you quickly find the correct spelling without leaving your workflow.

Under the hood, the application follows a layered architecture that separates concerns cleanly. The UI layer (built with Tkinter) handles user interaction and display, while the business logic lives in utility modules that are fully decoupled from the interface. A centralized error-handling system intercepts exceptions raised anywhere in the callback chain and displays them as user-friendly dialog boxes, so the user always receives meaningful feedback instead of a silent crash.

The application supports multiple environments (`development`, `production`, `testing`) via a config system driven by an `.env` file, making it easy to switch behavior between local development and a deployed executable. It can also be packaged into a standalone binary (`.exe` on Windows or a native binary on Linux/Mac) using PyInstaller, so end users can run it without installing Python.

The project is built with software quality in mind: it includes a full test suite (unit and integration tests with pytest), automated linting and formatting (ruff), pre-commit hooks to enforce code style on every commit, and dependency vulnerability scanning via pip-audit.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

#### Requirements.txt

```
pyspellchecker==0.8.3
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/word-sentry`](https://www.diegolibonati.com.ar/#/project/word-sentry)

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Known Issues

None at the moment.