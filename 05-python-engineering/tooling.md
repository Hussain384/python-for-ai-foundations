# Tooling Intro: pytest, ruff, black, mypy

Just an introduction. Add each tool only when a project is big enough to benefit; don't add all of them at the start.

| Tool | Job | JS / PHP equivalent | Add it when |
|---|---|---|---|
| **pytest** | runs your tests | jest / PHPUnit | you have functions you keep changing |
| **ruff** | linter: finds unused imports, undefined names, likely bugs | ESLint / PHPStan | a project has several files |
| **black** | formatter: rewrites code into one consistent style | Prettier / PHP-CS-Fixer | style differences cause noise |
| **mypy** | type checker: reads your type hints and finds mismatches | TypeScript / PHPStan | you use type hints widely |

## Install (inside your venv)
```bash
python -m pip install pytest ruff black mypy
```

## Use
```bash
python -m pytest          # run tests in tests/
ruff check .              # report problems
black .                   # format all files
mypy src                  # check types
```

## Quick examples
- **pytest** finds `test_*.py` files and `test_*` functions and uses plain `assert` (see `testing_basics.py`).
- **ruff** would flag `import os` when `os` is never used.
- **black** turns `x = {'a':1,'b':2}` into `x = {"a": 1, "b": 2}`.
- **mypy** would flag `greet(123)` when `greet` is hinted as `name: str` (see `type_hints.py`).

## Order to learn them
1. pytest (first and most useful)
2. black and ruff (keep code clean)
3. mypy (once you use type hints)
