"""Packages: where imports come from and how to check what is installed."""

import importlib.metadata as metadata
import importlib.util
import json
import sys

# module = one .py file, package = folder of modules,
# distribution = what `pip install` downloads.
print("json comes from:", json.__file__)

# Imports are searched in order: script folder, standard library, site-packages.
print("interpreter:", sys.executable)
print("inside a venv:", sys.prefix != sys.base_prefix)


def is_installed(name):
    return importlib.util.find_spec(name) is not None


for name in ["json", "pip", "numpy"]:
    print(name, "installed:", is_installed(name))

try:
    print("pip version:", metadata.version("pip"))
except metadata.PackageNotFoundError:
    print("pip not found")

# Gotcha: a local file named json.py or logging.py shadows the standard library.

# Commands (run in a terminal, inside a venv):
#   python -m pip install requests
#   python -m pip freeze > requirements.txt
#   python -m pip install -r requirements.txt
