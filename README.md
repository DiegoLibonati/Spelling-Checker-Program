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

#### Runtime (`[project.dependencies]`)

```
pyspellchecker==0.8.3
python-dotenv==1.2.2
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
mypy==1.13.0
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==9.0.3
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build (`[project.optional-dependencies]` build)

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

When preparing a production build, set `ENVIRONMENT=production` (and any other production values) directly in `.env`.

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

> **Warning:** `app.spec` bundles the repo-level `.env` file into the binary. Before building for production, set your production values directly in `.env`. **Never commit real secrets to the repo-level `.env`**.

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

## Continuous Integration

The repository ships with a **GitHub Actions** pipeline defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). It runs automatically on every `push` and `pull_request` targeting the `main` branch. On `push` to `main`, the same workflow continues with three additional jobs that produce an automated release.

### Pipeline overview

```
                      ┌─── PR or push to main ───┐
                      ▼                          ▼
┌──────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│   lint-and-audit     │─▶│       test       │─▶│      build       │
│ ruff · mypy · audit  │  │ pytest (headless)│  │ pyinstaller (lnx)│
└──────────────────────┘  └──────────────────┘  └──────────────────┘
                                                          │
                                       (only on push to main, sequentially)
                                                          ▼
                                                ┌──────────────────────┐
                                                │   prepare-release    │
                                                │ bump · changelog · tag│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │  build-windows-exe   │
                                                │ pyinstaller (windows)│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │   publish-release    │
                                                │ GitHub Release + .exe│
                                                └──────────────────────┘
```

### Validation jobs (run on every PR and push)

1. **`lint-and-audit`** — `ruff check`, `ruff format --check`, `mypy`, `pip-audit --skip-editable`.
2. **`test`** — installs Tkinter + `xvfb` on Ubuntu and runs `pytest --tb=short` headlessly.
3. **`build`** — smoke test that `pyinstaller app.spec` produces a binary on Linux.

### Release jobs (only on push to `main`)

4. **`prepare-release`** — inspects the commits since the latest tag, decides the next SemVer version using [Conventional Commits](#conventional-commits-required-for-releases), generates the changelog section, updates `CHANGELOG.md` and `pyproject.toml`, then commits, tags and pushes back to `main`. Skipped automatically when the head commit is the bot's own `chore(release): vX.Y.Z` commit, to avoid loops.
5. **`build-windows-exe`** — checks out the freshly created tag on a `windows-latest` runner, runs `pyinstaller app.spec`, and renames the artifact to `word-sentry-vX.Y.Z-windows.exe`.
6. **`publish-release`** — creates the GitHub Release for the new tag, attaches the Windows `.exe`, and uses the generated changelog section as the release notes.

### Conventional Commits (required for releases)

Commits merged into `main` must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so the pipeline can compute the next version and group the changelog entries.

| Commit prefix | Version bump | Example |
|---|---|---|
| `feat:` / `feat(scope):` | **MINOR** | `feat(ui): add dark mode toggle` |
| `fix:` / `fix(scope):` | **PATCH** | `fix: prevent crash on empty input` |
| `perf:`, `refactor:`, `docs:`, `build:`, `ci:`, `chore:`, `style:`, `test:` | **PATCH** | `refactor: extract spellcheck helper` |
| `feat!:` / `fix!:` or `BREAKING CHANGE:` in the body | **MAJOR** | `feat!: rewrite spellcheck API` |

When a push contains multiple commits, the highest applicable bump wins (a single `feat:` among many `fix:` triggers a MINOR bump). If you squash-merge PRs, configure the repo to use the PR title as the squash commit message and write the **PR title** following the convention.

### Skipping a release

If you need to push a change to `main` without producing a release (e.g. tweaking job names in the workflow, fixing a typo in the README), append `[skip release]` to the commit message. The validation jobs (lint, test, build) still run; only `prepare-release`, `build-windows-exe` and `publish-release` are skipped.

```bash
git commit -m "ci: rename build job for clarity [skip release]"
```

To skip **everything** including validation, use GitHub's standard `[skip ci]` marker instead.

### Where the build outputs live

| Output | Location |
|---|---|
| Validation logs (lint, tests) | **Actions** tab on GitHub |
| Linux smoke-build binary | Ephemeral, inside the runner |
| Windows `.exe` per version | **Releases** page (sidebar of the repo) |
| Version history & notes | [`CHANGELOG.md`](CHANGELOG.md) + Releases page |

> **Note:** GitHub's **Packages** section is for package registries (npm, PyPI, Docker, etc.) and does not host PyInstaller executables. Standalone binaries always live under **Releases**.

### Repository setup required for releases

For the release jobs to push tags and commits back to `main`, the repository needs:

1. **Settings → Actions → General → Workflow permissions**: set to *Read and write permissions*.
2. **Branch protection on `main`**: if enabled, allow the `github-actions[bot]` to bypass the PR requirement, or disable the protection for the bot. Otherwise `prepare-release` will fail when pushing the version bump.

### Running the same checks locally

```bash
# lint-and-audit
ruff check .
ruff format --check .
mypy --config-file=pyproject.toml .
pip-audit --skip-editable

# test
pytest --tb=short

# build
pyinstaller app.spec
```

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/word-sentry`](https://www.diegolibonati.com.ar/#/project/word-sentry)
