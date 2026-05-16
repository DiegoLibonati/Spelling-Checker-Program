# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Entries below this header are appended automatically by the CI release workflow
on every push to `main`. See the [Releases page](../../releases) for downloadable
binaries.
## [v1.1.0] - 2026-05-16

### Features

- feat(ci): add release automation pipeline and mypy type checking (36f6307)
- feat: .python-version file added (55da95d)
- feat: added new test step in CI (e5eb133)
- feat: added ci lint - ruff - audit - build (a7edcd0)
- feat: remove loggers info (01252a8)
- feat: better readme (342963a)
- feat: new pip audit - new requirements.dev.txt - better utils names (1404e39)
- feat: better error handler (bafeeba)
- feat: added test_dialogs.py (f2fe94f)
- feat: better structure by tkinter template (6c98505)
- feat: new fixture pytest spellchecker (900cd41)
- feat: re-organize files (954d4cb)
- feat: better structure tkinter project (f1b4ac4)
- feat: better exports - new build system and pre-commit added (d3434ba)
- feat: new structure project with tests (cec8a0e)

### Bug fixes

- fix: redirect egg-info to project root to prevent it from being generated inside src/ (f2b0e1a)
- fix: make .env bundling optional in app.spec for CI compatibility (d487a91)
- fix: resolve cross-platform spellchecker resources path in app.spec (0773686)
- fix: fix vulnerabilities (13ca69a)
- fix: better tests (1f683c8)
- fix: title app (b0bfa22)
- fix: better repository name and better system test (c079363)
- fix: remove migrations exclude in pre commit config and update requirements dev (98198c5)
- fix: test components and views folder rename (8cfe25b)
- fix: better constants (b08ed48)
- fix: fix build exe with nex config app.spec (cca49b4)
- fix: fix tests textblob to new library (74142b5)
- fix: fix build.bat and build.sh with new spellchecker library added (02c6851)
- fix: fix import names (64d5b59)

### Refactors

- refactor: replace pip install -r with pip install -e for build deps (a96c857)
- refactor: migrate deps to pyproject.toml and update README. (7aeea22)
- refactor: test suite to align with project testing standards and structure standars (893d044)
- refactor: test suite to align with project testing standards and structure standars (6bc1204)

### Documentation

- docs: simplify production env setup to use .env directly (31d5b66)

### Build & CI

- ci: run lint-and-audit, test, and build sequentially (378ffb4)

### Uncategorized

- patch: readme updated (2a0228a)
- patch: readme updated (fd6154f)
- patch: dependencies updated (c24bd18)
- patch: requirements.build.txt updated (6e324d4)
- patch: readme updated (3cb950e)
- patch: pyproject.toml update description (9e39644)
- patch: readme name (b42600c)
- patch: better name and description (784b3c5)
- patch: readme updated (e768ebc)
- patch: readme updated (5d72d60)
- patch: readme updated (3413a8b)
- Update README.md (3b5279c)
- New structure of project with types (e4cb4b8)
- Update README.md (aa745f4)
- fix link (fed447f)
- New readme, requirements, and code fix (321cb0f)
- Update README.md (82cce97)
- New readme (7cdd1ae)
- New repository! (d8e79f1)
- Initial commit (c39337f)

