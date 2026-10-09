"""Exercises: JSON and CSV representation and validation."""

import csv
import json
from pathlib import Path


def summarize_json(path: Path) -> None:
    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list) or any(
        not isinstance(record, dict) for record in records
    ):
        raise ValueError("JSON input must be a list of objects")

    expected_keys = set().union(*(record.keys() for record in records))
    print("JSON records:", len(records))
    missing_records = [
        (index, sorted(expected_keys - record.keys()))
        for index, record in enumerate(records, start=1)
        if expected_keys - record.keys()
    ]
    if missing_records:
        print("Missing keys:")
        for index, keys in missing_records:
            print(f"  Record {index}: {', '.join(keys)}")
    else:
        print("Missing keys: none")


def summarize_csv(path: Path) -> None:
    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError("CSV input must contain a header row")

        empty_cells = dict.fromkeys(reader.fieldnames, 0)
        row_count = 0
        for row in reader:
            row_count += 1
            for field in reader.fieldnames:
                value = row.get(field)
                if value is None or not value.strip():
                    empty_cells[field] += 1

    print("CSV columns:", reader.fieldnames)
    print("CSV rows:", row_count)
    columns_with_empty_cells = {
        field: count for field, count in empty_cells.items() if count
    }
    if columns_with_empty_cells:
        print("Empty cells:")
        for field, count in columns_with_empty_cells.items():
            print(f"  {field}: {count}")
    else:
        print("Empty cells: none")
    print("Numeric parsing: none; CSV values remain strings")


def main() -> None:
    data_directory = Path(__file__).resolve().parent.parent / "sample_data"
    json_path = data_directory / "support_tickets.json"
    csv_path = data_directory / "model_runs.csv"
    summarize_json(json_path)
    summarize_csv(csv_path)


if __name__ == "__main__":
    main()
