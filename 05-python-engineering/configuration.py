"""Configuration: keep settings in one place, not scattered through the code.

Order of priority (lowest to highest): defaults < config file < environment variables.
"""

import json
import os
from dataclasses import dataclass, replace
from pathlib import Path
from tempfile import TemporaryDirectory


@dataclass(frozen=True)  # frozen: settings can't change after they are built
class Settings:
    model_name: str = "example-model"
    temperature: float = 0.2
    debug: bool = False


def load_settings(config_path=None):
    settings = Settings()  # 1. defaults

    if config_path and Path(config_path).exists():  # 2. config file
        data = json.loads(Path(config_path).read_text(encoding="utf-8"))
        settings = replace(settings, **data)

    if "APP_TEMPERATURE" in os.environ:  # 3. environment (strings -> convert)
        settings = replace(settings, temperature=float(os.environ["APP_TEMPERATURE"]))
    if "APP_DEBUG" in os.environ:
        settings = replace(settings, debug=os.environ["APP_DEBUG"].lower() == "true")
    return settings


print("defaults:", load_settings())

with TemporaryDirectory() as directory:
    config_file = Path(directory) / "config.json"
    config_file.write_text(json.dumps({"temperature": 0.7}), encoding="utf-8")
    print("from file:", load_settings(config_file))

    os.environ["APP_TEMPERATURE"] = "1.0"
    print("env wins:", load_settings(config_file))

# Rules: load settings once at startup and pass the object around.
# Keep secrets (API keys) in environment variables, not in the config file.
