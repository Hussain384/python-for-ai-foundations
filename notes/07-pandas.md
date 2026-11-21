# 07. Pandas

Install inside your venv: `python -m pip install pandas`, then `import pandas as pd`.
Pandas is built on NumPy: a Series is a labeled 1-D array, a DataFrame is a table of Series.

## Series
- One labeled column: `pd.Series([142, 187], name="latency_ms")`.
- Has an index (labels) and values; custom labels allow `s["model-a"]`.
- `s.iloc[0]` by position, `s.loc["label"]` by label.
- Math is vectorized: `s / 1000`, `s > 150`, `s[s > 150]`.
- Useful: `.mean()`, `.describe()`, `.value_counts()`, `.unique()`, `.sort_values()`.
- Arithmetic matches labels, not positions; unmatched labels become `NaN`.

## DataFrame
- A table: `pd.DataFrame({"col": [...]})` or from a list of dicts (like JSON records).
- Inspect first: `df.shape`, `df.columns`, `df.dtypes`, `df.head()`, `df.info()`, `df.describe()`.
- `df["col"]` gives a Series; `df[["a", "b"]]` gives a DataFrame.
- `df.loc[row_label, "col"]` selects by label (slices include the end); `df.iloc[row_position]` selects by position.
- New column: `df["total"] = df["a"] + df["b"]`.
- `rename`, `drop`, `set_index`, `reset_index` return a new DataFrame; assign the result.

## Loading and exporting
- `pd.read_csv(path)` detects numbers automatically. Options: `usecols`, `dtype`, `na_values`, `sep`, `nrows`.
- `pd.read_json(path)` reads a list of objects; `pd.json_normalize(...)` flattens nested JSON.
- `df.to_csv(path, index=False)` and `df.to_json(path, orient="records", indent=2)`.
- Keep the original file; write cleaned data to a new file.
- Other formats: Excel, Parquet (common in ML), SQL.

## Filtering
- Boolean mask: `df[df["latency_ms"] < 150]`.
- Combine with `&`, `|`, `~` and put each condition in parentheses (not `and`/`or`/`not`).
- `isin([...])`, `between(a, b)`, `.str.startswith(...)`, `df.query("model == 'alpha'")`.
- `df.loc[condition, ["col1", "col2"]]` picks rows and columns together.
- A filter returns a new DataFrame; use `.copy()` before changing it.

## Sorting
- `df.sort_values("col", ascending=False)`, or several columns with a list.
- `df.nlargest(n, "col")` and `df.nsmallest(n, "col")`.

## Grouping
- Split -> apply -> combine: `df.groupby("model")["accuracy"].mean()`.
- Several results: `.agg(["mean", "min", "max"])` or named: `.agg(avg=("accuracy", "mean"))`.
- Group by several columns with a list; `.reset_index()` turns group names back into a column.
- `value_counts()` counts rows per value; `pivot_table(index=, columns=, values=, aggfunc=)` builds a summary table.
- `groupby(...).transform("mean")` returns a value for every original row.

## Missing values
- Missing values are `NaN` (or `None`/`NA`); `df.isna().sum()` counts them per column.
- Convert placeholders like `"N/A"` to missing with `replace` or `na_values`.
- Decide per column: `dropna(subset=[...])` removes rows; `fillna(value)` fills them (mean, median, a constant such as `"unknown"`).
- `dropna()` with no arguments can remove most of your data.
- Most aggregations like `mean()` skip `NaN`.

## Cleaning
- `drop_duplicates()` and `df.duplicated().sum()`.
- Text: `df["col"].str.strip().str.lower()`.
- Types: `pd.to_numeric(col, errors="coerce")` turns bad values into `NaN`; `astype(...)` converts types.
- Typical order: inspect -> placeholders -> text and types -> duplicates -> missing values -> transform -> save.

## Transforming
- Vectorized new columns: `df["is_urgent"] = df["priority"] == "high"`.
- `map({...})` for lookups, `apply(function)` row by row (slower; prefer vectorized or `.str`), `pd.cut(...)` for bins.
- Outlier check: values beyond `Q1 - 1.5*IQR` or `Q3 + 1.5*IQR`.

## Pandas 3 notes
- Don't use `inplace=True`; assign the result (`df = df.drop(...)`).
- Changing a filtered slice never changes the original, so no "chained assignment" tricks; assign with `df.loc[mask, "col"] = value`.
- Text columns show dtype `str`.

## Practice checklist
- [ ] build a Series with a custom index and filter it
- [ ] build a DataFrame and inspect it with shape, dtypes, head, info, describe
- [ ] load a CSV and a JSON file
- [ ] filter with two conditions and sort the result
- [ ] compute average and count per group
- [ ] count missing values per column
- [ ] clean text, fix types, drop duplicates, fill missing values
- [ ] add a new column from existing columns
- [ ] export the cleaned data to a new CSV
