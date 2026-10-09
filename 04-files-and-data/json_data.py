"""JSON serialization: Python values <-> portable text."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory


run_record = {
    "model": "example-instruct-model",
    "temperature": 0.2,
    "messages": [
        {"role": "user", "content": "Summarize the dataset."},
        {"role": "assistant", "content": "The dataset contains 12 records."},
    ],
    "usage": {"prompt_tokens": 18, "completion_tokens": 9},
}

with TemporaryDirectory(prefix="phase04-json-") as temporary_directory:
    sample_file = Path(temporary_directory) / "model_run.json"
    # JSON objects map naturally to dicts; arrays to lists; null to None;
    # booleans to bool; numbers and strings keep their corresponding types.
    with sample_file.open("w", encoding="utf-8") as file:
        json.dump(run_record, file, ensure_ascii=False, indent=2)
        file.write("\n")

    with sample_file.open("r", encoding="utf-8") as file:
        loaded_record = json.load(file)

    print("Model:", loaded_record["model"])
    print("Assistant:", loaded_record["messages"][1]["content"])
    print("Tokens:", loaded_record["usage"]["prompt_tokens"]
          + loaded_record["usage"]["completion_tokens"])

    # JSON text can also be converted without touching the filesystem.
    json_text = json.dumps({"status": "ready", "valid": True})
    print("Serialized:", json_text)
    print("Decoded:", json.loads(json_text))
