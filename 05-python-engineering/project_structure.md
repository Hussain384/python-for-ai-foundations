# Project Structure

Grow the layout only when the current one gets painful.

## 1. One script (phases 01-04)
```
analyze.py
```

## 2. A few modules
```
my_project/
├── main.py        # entry point: reads args, calls functions, prints results
├── config.py      # settings (model name, paths, env variables)
└── utils.py       # reusable functions
```
Split a file when it gets long or does unrelated jobs: `from utils import clean_text`.

## 3. A real project (typical AI/ML starting point)
```
my_project/
├── .venv/               # virtual environment (not committed)
├── .env                 # secrets, e.g. API keys (not committed)
├── .env.example         # fake values showing which variables are needed (committed)
├── .gitignore           # lists .venv/, .env, __pycache__/
├── requirements.txt     # dependencies (committed)
├── README.md            # what it is and how to run it
├── src/my_project/
│   ├── __init__.py      # marks a package; can be empty
│   ├── config.py
│   ├── data.py
│   └── main.py
└── tests/
    └── test_data.py
```

## What each part is for
| Item | Job | JS / PHP equivalent |
|---|---|---|
| `.venv/` | isolated Python and packages | `node_modules/`, `vendor/` |
| `requirements.txt` | dependency list | `package.json`, `composer.json` |
| `.env` | secrets and local settings | `.env` |
| `src/package/` | your code | `src/` |
| `__init__.py` | makes a folder importable | `index.js` |
| `tests/` | tests | `__tests__/`, `tests/` |

## Rules
- Keep logic in functions; keep printing and argument parsing in `main()`.
- Use `if __name__ == "__main__":` so a file runs only when executed directly, not when imported.
- Name files in `lowercase_with_underscores`; never reuse standard-library names (`json.py`, `logging.py`).
- Avoid two modules importing each other; move the shared code to a third module.
