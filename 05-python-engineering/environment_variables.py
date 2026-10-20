"""Environment variables: settings and secrets that live outside the code.

JS: process.env.API_KEY    PHP: getenv('API_KEY')
"""

import os

print(os.getenv("DEMO_API_KEY", "<not set>"))  # .get-style, with a default

os.environ["DEMO_API_KEY"] = "sk-demo-123"  # only affects this process
print(os.environ["DEMO_API_KEY"])  # [] raises KeyError if missing

# Values are always strings: convert them yourself.
os.environ["DEMO_DEBUG"] = "true"
os.environ["DEMO_RETRIES"] = "5"
debug = os.getenv("DEMO_DEBUG", "false").lower() in {"1", "true", "yes"}
retries = int(os.getenv("DEMO_RETRIES", "3"))
print(debug, retries)
print(bool("false"))  # True! any non-empty string is truthy


# Fail fast when a required variable is missing.
def require_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value


try:
    require_env("OPENAI_API_KEY_THAT_DOES_NOT_EXIST")
except RuntimeError as error:
    print(error)

# .env files: KEY=value lines for local development. Load them with
# python-dotenv (`from dotenv import load_dotenv; load_dotenv()`).
# Add .env to .gitignore; never commit secrets or print them.
