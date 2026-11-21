"""Cleaning: missing values, duplicates, text, types, and transformations."""

import numpy as np
import pandas as pd

# A deliberately messy dataset.
df = pd.DataFrame(
    {
        "ticket_id": ["T-1", "T-2", "T-2", "T-3", "T-4", "T-5"],
        "category": ["  Billing", "technical ", "technical ", "BILLING", None, "billing"],
        "priority": ["high", "low", "low", "N/A", "medium", "low"],
        "response_min": ["30", "45", "45", "abc", "20", None],
        "satisfaction": [4.5, np.nan, np.nan, 3.0, 5.0, 4.0],
    }
)
print(df)

# --- 1. find missing values --------------------------------------------------
print(df.isna())  # True where missing
print(df.isna().sum())  # missing count per column
print((df.isna().mean() * 100).round(1))  # percent missing per column
print(df[df["satisfaction"].isna()])  # the rows with a missing value

# --- 2. treat placeholders as missing ----------------------------------------
df = df.replace({"N/A": np.nan, "": np.nan})  # or read_csv(na_values=["N/A"])

# --- 3. drop duplicates ------------------------------------------------------
print(df.duplicated().sum(), "duplicate rows")
df = df.drop_duplicates()

# --- 4. clean text: .str methods work on whole columns -----------------------
df["category"] = df["category"].str.strip().str.lower()  # "  Billing" -> "billing"

# --- 5. fix types: invalid values become NaN with errors="coerce" ------------
df["response_min"] = pd.to_numeric(df["response_min"], errors="coerce")
print(df.dtypes)

# --- 6. handle missing values: drop OR fill (a decision, not a default) ------
print(df.dropna(subset=["category"]))  # drop rows missing a key column
print(df.dropna())  # drop rows with ANY missing value (can lose a lot)

df["satisfaction"] = df["satisfaction"].fillna(df["satisfaction"].median())
df["category"] = df["category"].fillna("unknown")
df["response_min"] = df["response_min"].fillna(df["response_min"].mean())
df["priority"] = df["priority"].fillna("unknown")
print(df.isna().sum().sum(), "missing values left")

# --- 7. transform: map, apply, new columns, bins -----------------------------
df["is_urgent"] = df["priority"] == "high"
df["priority_rank"] = df["priority"].map({"low": 1, "medium": 2, "high": 3, "unknown": 0})
df["speed"] = pd.cut(df["response_min"], bins=[0, 25, 40, 100], labels=["fast", "ok", "slow"])
df["category"] = df["category"].apply(lambda text: text.title())  # row-by-row: slower, use .str when you can
print(df)

# --- 8. rename and reorder columns, reset the index --------------------------
df = df.rename(columns={"response_min": "response_minutes"})
df = df[["ticket_id", "category", "priority", "response_minutes", "satisfaction"]]
df = df.reset_index(drop=True)
print(df)

# --- 9. outliers: a quick check with a simple rule ---------------------------
values = pd.Series([10, 12, 11, 13, 200])
q1, q3 = values.quantile(0.25), values.quantile(0.75)
spread = q3 - q1
print(values[(values < q1 - 1.5 * spread) | (values > q3 + 1.5 * spread)])  # 200

# Workflow: inspect -> find missing -> fix types/text -> duplicates -> decide
# on missing values -> transform -> save to a NEW file (keep the original).
