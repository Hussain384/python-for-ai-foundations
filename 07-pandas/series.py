"""Series: one labeled column of data (a NumPy array plus an index).

Install first (inside your venv):  python -m pip install pandas
"""

import pandas as pd

# --- create a Series ---------------------------------------------------------
latency = pd.Series([142, 187, 131, 205], name="latency_ms")
print(latency)  # left = index (labels), right = values
print(latency.dtype, latency.shape, len(latency))

# --- custom index: labels instead of 0, 1, 2 ---------------------------------
accuracy = pd.Series([0.91, 0.87, 0.95], index=["model-a", "model-b", "model-c"])
print(accuracy["model-b"])  # by label  -> 0.87
print(accuracy.iloc[0])  # by position -> 0.91
print(accuracy[["model-a", "model-c"]])  # several labels

# --- from a dict: keys become the index --------------------------------------
tokens = pd.Series({"prompt": 18, "completion": 9})
print(tokens)

# --- vectorized math, just like NumPy ----------------------------------------
print(latency / 1000)  # seconds
print(latency * 2)
print(latency > 150)  # boolean Series
print(latency[latency > 150])  # filter with a mask

# --- common methods ----------------------------------------------------------
print(latency.mean(), latency.max(), latency.min(), latency.std())
print(latency.describe())  # count, mean, std, min, quartiles, max
print(latency.sort_values(ascending=False))
print(latency.head(2))

# --- value_counts: how often each value appears ------------------------------
models = pd.Series(["alpha", "beta", "alpha", "alpha", "beta"])
print(models.value_counts())
print(models.unique())  # distinct values

# --- missing values ----------------------------------------------------------
scores = pd.Series([0.9, None, 0.7])  # None becomes NaN ("not a number")
print(scores)
print(scores.isna())  # [False  True False]
print(scores.mean())  # NaN is skipped -> 0.8

# --- aligned arithmetic: pandas matches labels, not positions ----------------
a = pd.Series([1, 2], index=["x", "y"])
b = pd.Series([10, 20], index=["y", "z"])
print(a + b)  # only "y" exists in both; x and z become NaN

# A DataFrame is a table made of Series that share one index (see dataframes.py).
