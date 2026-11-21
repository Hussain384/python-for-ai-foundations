"""DataFrame: a table of rows and columns. Each column is a Series."""

import pandas as pd

# --- create from a dict of columns -------------------------------------------
df = pd.DataFrame(
    {
        "run_id": ["run-001", "run-002", "run-003", "run-004"],
        "model": ["alpha", "beta", "alpha", "beta"],
        "latency_ms": [142, 187, 131, 205],
        "prompt_tokens": [18, 18, 22, 22],
        "completion_tokens": [9, 12, 8, 11],
    }
)

# --- or from a list of records (like a JSON array of objects) ----------------
records = [{"name": "Ada", "score": 0.9}, {"name": "Linus", "score": 0.7}]
print(pd.DataFrame(records))

# --- inspect the structure: do this first with any new dataset ---------------
print(df.shape)  # (rows, columns) -> (4, 5)
print(df.columns.tolist())
print(df.dtypes)  # type of each column
print(df.head(2))  # first rows; .tail() for the last
df.info()  # columns, non-null counts, memory
print(df.describe())  # statistics for numeric columns

# --- select columns ----------------------------------------------------------
print(df["model"])  # one column -> Series
print(df[["model", "latency_ms"]])  # list of columns -> DataFrame

# --- select rows: loc = by label, iloc = by position -------------------------
print(df.iloc[0])  # first row
print(df.iloc[1:3])  # rows 1 and 2
print(df.loc[0, "model"])  # row label 0, column "model"
print(df.loc[:, "model":"latency_ms"])  # label slices INCLUDE the end

# --- add and change columns (vectorized, no loops) ---------------------------
df["total_tokens"] = df["prompt_tokens"] + df["completion_tokens"]
df["latency_s"] = df["latency_ms"] / 1000
print(df)

# --- rename, drop: these return a new DataFrame, so assign the result --------
df = df.rename(columns={"latency_s": "latency_seconds"})
df = df.drop(columns=["latency_seconds"])
print(df.columns.tolist())

# --- index: row labels --------------------------------------------------------
by_id = df.set_index("run_id")
print(by_id.loc["run-002", "model"])  # look up a row by its id
print(by_id.reset_index().columns.tolist())  # back to a normal column

# --- convert -----------------------------------------------------------------
print(df.to_dict(orient="records")[0])  # list of dicts, like phase 04 JSON
print(df["latency_ms"].to_numpy())  # NumPy array (pandas is built on NumPy)

# Inspect first: shape, dtypes, head, info, describe. Then work.
