"""Clean and summarize a JSON or CSV file containing object records."""

import argparse
import csv
import json
import math
import statistics
import sys
from pathlib import Path


def read_records(path: Path) -> list[dict]:
    """Load a JSON list of objects or CSV table into records."""
    suffix = path.suffix.casefold()
    if suffix == ".json":
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list) or any(not isinstance(row, dict) for row in data):
            raise ValueError("JSON input must be a list of objects")
        return data
    if suffix == ".csv":
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames is None:
                raise ValueError("CSV input must contain a header row")
            return list(reader)
    raise ValueError("input file must have a .json or .csv extension")


def clean_records(records: list[dict]) -> tuple[list[dict], int]:
    """Trim string values and remove wholly blank records; retain other values."""
    cleaned = []
    removed = 0
    for record in records:
        row = {
            key.strip() if isinstance(key, str) else key:
            value.strip() if isinstance(value, str) else value
            for key, value in record.items()
        }
        if not row or all(value == "" or value is None for value in row.values()):
            removed += 1
            continue
        cleaned.append(row)
    return cleaned, removed


def numeric_statistics(records: list[dict]) -> dict[str, dict[str, float]]:
    """Summarize columns whose non-empty values all parse as finite numbers."""
    if not records:
        return {}

    stats = {}
    for key in records[0]:
        values = []
        for record in records:
            value = record.get(key)
            if value is None or value == "":
                continue
            if isinstance(value, bool):
                break
            try:
                number = float(value)
            except (TypeError, ValueError):
                break
            if not math.isfinite(number):
                break
            values.append(number)
        else:
            if values:
                stats[str(key)] = {
                    "count": len(values),
                    "mean": statistics.fmean(values),
                    "min": min(values),
                    "max": max(values),
                }
    return stats


def write_records(path: Path, records: list[dict]) -> None:
    """Write JSON or CSV records, creating destination directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.casefold()
    if suffix == ".json":
        with path.open("w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
            file.write("\n")
        return
    if suffix == ".csv":
        fieldnames = list(dict.fromkeys(key for row in records for key in row))
        with path.open("w", newline="", encoding="utf-8") as file:
            if not fieldnames:
                return
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="raise")
            writer.writeheader()
            writer.writerows(records)
        return
    raise ValueError("output file must have a .json or .csv extension")


def process_dataset(input_path: Path, output_path: Path) -> dict:
    """Run load -> clean -> summarize -> persist; return a report."""
    if input_path.resolve() == output_path.resolve():
        raise ValueError("input and output paths must be different")
    records = read_records(input_path)
    cleaned, removed = clean_records(records)
    write_records(output_path, cleaned)
    return {
        "input_records": len(records),
        "output_records": len(cleaned),
        "blank_records_removed": removed,
        "numeric_statistics": numeric_statistics(cleaned),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="input .json or .csv file")
    parser.add_argument("output", type=Path, help="output .json or .csv file")
    args = parser.parse_args()

    try:
        report = process_dataset(args.input, args.output)
    except (OSError, UnicodeError, json.JSONDecodeError, csv.Error, ValueError) as error:
        parser.error(str(error))

    print(f"Input records: {report['input_records']}")
    print(f"Output records: {report['output_records']}")
    print(f"Blank records removed: {report['blank_records_removed']}")
    print(f"Processed dataset: {args.output}")
    print("Numeric statistics:")
    if report["numeric_statistics"]:
        for column, values in report["numeric_statistics"].items():
            print(
                f"  {column}: n={values['count']}, mean={values['mean']:.2f}, "
                f"min={values['min']:.2f}, max={values['max']:.2f}"
            )
    else:
        print("  (no numeric columns)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
