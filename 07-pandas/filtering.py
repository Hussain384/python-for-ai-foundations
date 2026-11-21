"""Filtering and sorting rows."""

import pandas as pd

df = pd.DataFrame(
    {
        "run_id": ["r1", "r2", "r3", "r4", "r5", "r6"],
        "model": ["alpha", "beta", "alpha", "beta", "gamma", "alpha"],
        "dataset": ["v1", "v1", "v2", "v2", "v1", "v2"],
        "latency_ms": [142, 187, 131, 205, 99, 160],
        "accuracy": [0.91, 0.87, 0.93, 0.82, 0.95, 0.89],
    }
)

# --- boolean filter: condition -> True/False per row -> keep the True rows ----
print(df[df["latency_ms"] < 150])
print(df[df["model"] == "alpha"])

# --- combine conditions: & (and), | (or), ~ (not); wrap EACH in parentheses --
print(df[(df["model"] == "alpha") & (df["accuracy"] > 0.9)])
print(df[(df["model"] == "gamma") | (df["latency_ms"] > 200)])
print(df[~(df["dataset"] == "v1")])
# Gotcha: use & | ~ here, NOT the words and / or / not.

# --- isin, between, string matching ------------------------------------------
print(df[df["model"].isin(["alpha", "gamma"])])
print(df[df["accuracy"].between(0.88, 0.92)])  # inclusive on both ends
print(df[df["run_id"].str.startswith("r1")])

# --- query: filter with a readable string ------------------------------------
print(df.query("model == 'alpha' and latency_ms < 150"))

# --- pick rows AND columns at once with loc ----------------------------------
print(df.loc[df["accuracy"] > 0.9, ["model", "accuracy"]])

# --- sorting -----------------------------------------------------------------
print(df.sort_values("latency_ms"))  # ascending (smallest first)
print(df.sort_values("accuracy", ascending=False))  # best first
print(df.sort_values(["model", "latency_ms"], ascending=[True, False]))  # by 2 columns
print(df.nlargest(2, "accuracy"))  # top 2 by accuracy
print(df.nsmallest(2, "latency_ms"))  # 2 fastest

# --- counting ----------------------------------------------------------------
print((df["accuracy"] > 0.9).sum())  # True counts as 1 -> how many rows match
print(len(df[df["accuracy"] > 0.9]))  # same, by counting filtered rows

# A filter returns a NEW DataFrame; the original is unchanged.
good = df[df["accuracy"] > 0.9].copy()  # .copy() before changing a filtered result
good["status"] = "good"
