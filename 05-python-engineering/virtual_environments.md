# Virtual Environments

A venv is a private folder with its own Python and installed packages, so each project has its own dependencies.

| | JavaScript | PHP | Python |
|---|---|---|---|
| Packages live in | `node_modules/` | `vendor/` | `.venv/` |
| Manifest | `package.json` | `composer.json` | `requirements.txt` |
| Install | `npm install` | `composer install` | `python -m pip install -r requirements.txt` |

Unlike npm/composer, Python only uses the venv if you **activate** it.

## Commands
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1        # Git Bash: source .venv/Scripts/activate
python -m pip install requests
python -m pip freeze > requirements.txt
deactivate
```

## Rules
- One venv per project, named `.venv`, inside the project folder.
- Put `.venv/` in `.gitignore`; commit `requirements.txt` instead.
- To rebuild: create a new venv and run `pip install -r requirements.txt`.
- If PowerShell blocks activation: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
- Later options: `uv` (faster), `conda` (common in data science).

## Virtual environment vs package management
| | Virtual environment | Package management |
|---|---|---|
| Question | **Where** are packages installed? | **What** is installed, and which versions? |
| Tool | `python -m venv` | `pip` and `requirements.txt` |
| JS/PHP | the `node_modules/` or `vendor/` folder | `npm install` / `composer require` |

Create the venv once, activate it, then use pip inside it. Without a venv, pip installs into your global Python.

## Virtual environment vs environment variables
| | Virtual environment | Environment variables |
|---|---|---|
| What | an isolated folder of Python and libraries | named string values passed to a program |
| Purpose | separate project dependencies | keep settings and secrets out of code |
| Example | `.venv/` with `numpy` | `OPENAI_API_KEY=sk-...` in `.env` |

Unrelated problems. Activating a venv does not load your `.env` file. A typical AI project has both: the venv holds `openai` and `numpy`, and `.env` holds the API key.
