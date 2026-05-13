# Word Sentry

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Word Sentry** is a desktop application built with Python and Tkinter that helps users identify and correct spelling mistakes in real time. The application provides a clean and minimal graphical interface where the user types a word into an input field and, upon clicking the check button, receives a list of spelling suggestions powered by the `pyspellchecker` library.

The core use case is straightforward: if you are unsure whether a word is spelled correctly, you type it in and the application returns the closest matching words from its dictionary. For example, typing `recieve` will return suggestions like `receive`, helping you quickly find the correct spelling without leaving your workflow.

Under the hood, the application follows a layered architecture that separates concerns cleanly. The UI layer (built with Tkinter) handles user interaction and display, while the business logic lives in utility modules that are fully decoupled from the interface. A centralized error-handling system intercepts exceptions raised anywhere in the callback chain and displays them as user-friendly dialog boxes, so the user always receives meaningful feedback instead of a silent crash.

The application supports multiple environments (`development`, `production`, `testing`) via a config system driven by an `.env` file, making it easy to switch behavior between local development and a deployed executable. It can also be packaged into a standalone binary (`.exe` on Windows or a native binary on Linux/Mac) using PyInstaller, so end users can run it without installing Python.

The project is built with software quality in mind: it includes a full test suite (unit and integration tests with pytest), automated linting and formatting (ruff), pre-commit hooks to enforce code style on every commit, and dependency vulnerability scanning via pip-audit.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

All dependencies are declared in `pyproject.toml`. The `requirements*.txt` files are thin wrappers that delegate to it.

**Runtime (`[project.dependencies]`)**

```
pyspellchecker==0.8.3
python-dotenv==1.0.1
```

**Dev (`[project.optional-dependencies] dev`)**

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

**Test (`[project.optional-dependencies] test`)**

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

**Build (`[project.optional-dependencies] build`)**

```
pyinstaller==6.16.0
```

## Getting Started

Follow these steps to set up the project locally:

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .[dev,test]`
6. Copy the example environment file so the app can load its config:
   - Windows: `copy .env.example.dev .env`
   - Linux/Mac: `cp .env.example.dev .env`
7. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

Once the virtual environment is active and dev dependencies are installed, wire up the pre-commit hooks so linting and formatting run automatically before every commit:

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The `.env` file you copied during setup controls which config class the app loads at startup. The variables it accepts are:

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

There is also an `.env.example.prod` file that mirrors the production defaults — copy it to `.env` when preparing a production build.

## Testing

With the environment configured, you can verify the codebase by running the full pytest suite:

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .[test]`
6. Execute: `pytest --log-cli-level=INFO`

You can also filter by marker (`pytest -m unit`, `pytest -m integration`) or run a single test file/name with `pytest tests/path/to/test_file.py` or `pytest -k "test_function_name"`.

## Security Audit

Once tests pass, scan the runtime dependencies for known vulnerabilities using **pip-audit** before shipping:

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e .[dev]`
4. Execute: `pip-audit`

## Build

With tests green and no critical advisories from the audit, generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

> **Warning:** `app.spec` bundles the repo-level `.env` file into the binary. Before building for production, create a separate `.env.prod` file with your production values, update the `datas` entry in `app.spec` to reference `.env.prod` instead of `.env`, and **never commit real secrets to the repo-level `.env`**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e .[build]`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e .[build]`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/word-sentry`](https://www.diegolibonati.com.ar/#/project/word-sentry)
