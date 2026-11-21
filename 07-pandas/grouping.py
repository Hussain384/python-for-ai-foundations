"""Grouping: split rows into groups, calculate something per group, combine."""

import pandas as pd

df = pd.DataFrame(
    {
        "model": ["alpha", "beta", "alpha", "beta", "gamma", "alpha"],
        "dataset": ["v1", "v1", "v2", "v2", "v1", "v2"],
        "latency_ms": [142, 187, 131, 205, 99, 160],
        "accuracy": [0.91, 0.87, 0.93, 0.82, 0.95, 0.89],
    }
)

# --- groupby + one aggregation (like SQL GROUP BY) ---------------------------
print(df.groupby("model")["accuracy"].mean())  # average accuracy per model
print(df.groupby("model")["latency_ms"].max())

# --- counting rows per group -------------------------------------------------
print(df["model"].value_counts())  # quick count of one column
print(df.groupby("model").size())  # same idea, sorted by group name

# --- several aggregations at once --------------------------------------------
print(df.groupby("model")["accuracy"].agg(["mean", "min", "max", "count"]))

# --- named aggregation: different columns, readable result names -------------
summary = df.groupby("model").agg(
    runs=("accuracy", "count"),
    avg_accuracy=("accuracy", "mean"),
    avg_latency=("latency_ms", "mean"),
)
print(summary)
print(summary.reset_index())  # turn the group names back into a normal column

# --- group by two columns ----------------------------------------------------
print(df.groupby(["model", "dataset"])["accuracy"].mean())

# --- pivot table: groups as rows AND columns (a spreadsheet-style summary) ---
print(df.pivot_table(index="model", columns="dataset", values="accuracy", aggfunc="mean"))

# --- add a per-group value back onto every row -------------------------------
df["model_avg_accuracy"] = df.groupby("model")["accuracy"].transform("mean")
df["vs_model_avg"] = df["accuracy"] - df["model_avg_accuracy"]
print(df)

# --- sort a grouped result ---------------------------------------------------
print(summary.sort_values("avg_accuracy", ascending=False))

# Pattern: split (groupby) -> apply (mean/count/...) -> combine (a new table).
