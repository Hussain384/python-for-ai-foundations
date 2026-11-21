"""Loading and exporting data: CSV and JSON in, CSV and JSON out."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd

# Reuse the sample files from phase 04, located relative to this script.
SAMPLE_DATA = Path(__file__).resolve().parent.parent / "04-files-and-data" / "sample_data"

# --- loading CSV -------------------------------------------------------------
runs = pd.read_csv(SAMPLE_DATA / "model_runs.csv")
print(runs.head())
print(runs.dtypes)  # numbers are detected automatically (phase 04: all strings)

# Useful read_csv options:
#   usecols=["model", "latency_ms"]   load only some columns
#   dtype={"run_id": "string"}        force a type
#   na_values=["N/A", "-"]            extra strings to treat as missing
#   sep=";"                           different delimiter
#   nrows=100                         read only the first 100 rows (big files)
#   encoding="utf-8"

# --- loading JSON (a list of objects) ----------------------------------------
tickets = pd.read_json(SAMPLE_DATA / "support_tickets.json")
print(tickets)

# Nested JSON (objects inside objects) can be flattened:
nested = [{"model": "alpha", "usage": {"prompt": 18, "completion": 9}}]
print(pd.json_normalize(nested))  # columns: model, usage.prompt, usage.completion

# --- exporting ---------------------------------------------------------------
with TemporaryDirectory(prefix="phase07-") as directory:
    out = Path(directory)

    fast = runs[runs["latency_ms"] < 190]
    fast.to_csv(out / "fast_runs.csv", index=False)  # index=False: no extra id column
    fast.to_json(out / "fast_runs.json", orient="records", indent=2)

    print((out / "fast_runs.csv").read_text(encoding="utf-8"))

    reloaded = pd.read_csv(out / "fast_runs.csv")  # round trip
    print(reloaded.shape)

# Other formats exist: read_excel, read_parquet (common for big ML datasets), read_sql.
# Always keep the original file; save cleaned data to a new file (as in phase 04).
