# 05. Python Engineering

## Exceptions
- `try` / `except` / `else` / `finally`; `else` runs if nothing raised, `finally` always runs.
- Catch specific errors (`ValueError`, `KeyError`), not a bare `except:`.
- `raise ValueError("message")` to signal a problem; subclass `Exception` for your own errors.
- Python style: try it and handle failure, rather than checking first.

## Logging
- Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL.
- `logging.basicConfig(...)` once at startup; `logging.getLogger(__name__)` per module.
- `logger.exception(...)` inside `except` logs the traceback.
- `print` is for output; logging is for diagnostics. Never log secrets.

## Environment variables
- `os.getenv("X", default)` or `os.environ["X"]` (KeyError if missing).
- Values are always strings; convert them yourself (`bool("false")` is `True`).
- Keep API keys in a git-ignored `.env` file; load it with `python-dotenv`.

## Virtual environments
- `python -m venv .venv`, activate it, then `python -m pip install ...`.
- One per project; never commit it. See `05-python-engineering/virtual_environments.md`.
- Venv = *where* packages live; package management (pip) = *what* gets installed; environment variables = settings/secrets. Three different things.

## Package management
- `pip install`, `pip freeze > requirements.txt`, `pip install -r requirements.txt`.
- Always use `python -m pip` so pip matches your interpreter.
- Never name a file after a standard-library module (`json.py`, `logging.py`).

## Project structure and configuration
- Start with one script; split into modules when a file gets long.
- Keep settings (model name, paths, keys) in one place: constants, a config file, or env vars.
- Keep logic in functions; keep the CLI/printing in a small `main()`.
- Typical layout: `.venv/`, `.env`, `.gitignore`, `requirements.txt`, `src/package/`, `tests/`. See `05-python-engineering/project_structure.md` and `configuration.py`.

## Type hints
- Optional documentation: `def f(x: int, name: str | None = None) -> list[float]:`.
- Python does not enforce them; tools like mypy read them.

## Testing basics
- A test calls a function and `assert`s the result.
- `pytest` finds `test_*.py` files and `test_*` functions.
- `pytest.raises(ValueError)` checks an expected error.

## Tools (add later, not now; intro in `05-python-engineering/tooling.md`)
- **pytest** when you have functions you keep changing.
- **ruff** (lint) and **black** (format) once a project has several files.
- **mypy** once you use type hints widely.

## Practice checklist
- [ ] catch and raise specific exceptions
- [ ] use logging instead of print for debugging
- [ ] read a setting from an environment variable
- [ ] create and activate a virtual environment
- [ ] install a package and freeze requirements
- [ ] write one pytest test
- [ ] sketch a project folder layout with `.venv`, `.env`, `src/`, `tests/`
- [ ] add type hints to one function
