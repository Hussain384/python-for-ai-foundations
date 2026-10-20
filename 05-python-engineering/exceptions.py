"""Exceptions: handle errors on purpose (JS try/catch, PHP try/catch)."""

import json

# try / except / else / finally
try:
    value = float("hot")
except ValueError as error:  # catch the specific error, never a bare `except:`
    print("not a number:", error)
    value = None
else:  # runs only if nothing was raised
    print("parsed", value)
finally:  # always runs
    print("done")

# raise your own errors
def set_temperature(value):
    if not 0 <= value <= 2:
        raise ValueError(f"temperature must be 0-2, got {value}")
    return value


try:
    set_temperature(5)
except ValueError as error:
    print("caught:", error)

# custom exception
class DatasetError(Exception):
    pass


try:
    json.loads("{broken")
except json.JSONDecodeError as error:
    print("bad JSON:", error.msg)

# Python style (EAFP): try it and handle failure, instead of checking first.
settings = {"timeout": 10}
try:
    timeout = settings["timeout"]
except KeyError:
    timeout = 30
print("timeout:", timeout)
