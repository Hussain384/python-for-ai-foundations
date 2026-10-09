"""CSV reading and writing using the standard-library csv module."""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory


experiments = [
    {"run_id": "run-001", "model": "model-a", "latency_ms": 142, "success": True},
    {"run_id": "run-002", "model": "model-b", "latency_ms": 187, "success": False},
]

with TemporaryDirectory(prefix="phase04-csv-") as temporary_directory:
    sample_file = Path(temporary_directory) / "experiments.csv"
    # newline="" lets csv handle platform-specific newline rules correctly.
    with sample_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=experiments[0].keys())
        writer.writeheader()
        writer.writerows(experiments)

    with sample_file.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # CSV has text cells. Convert types deliberately at the application boundary.
    typed_rows = [
        {
            **row,
            "latency_ms": int(row["latency_ms"]),
            "success": row["success"].casefold() == "true",
        }
        for row in rows
    ]
    print("Columns:", reader.fieldnames)
    for row in typed_rows:
        print(row)
    print("Average latency:", sum(row["latency_ms"] for row in typed_rows) / len(typed_rows))
