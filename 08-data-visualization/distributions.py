"""Distributions: histograms, box plots, and what shape your data has."""

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=42)  # seeded: same data every run

# A distribution = how often each value (or range of values) appears.
normal = rng.normal(loc=0, scale=1, size=1000)  # bell curve: mean 0, std 1
skewed = rng.exponential(scale=1.0, size=1000)  # many small values, a few large

# --- histogram: count values in bins -----------------------------------------
fig, ax = plt.subplots()
ax.hist(normal, bins=30, color="tab:blue", edgecolor="white")
ax.set_title("Histogram of normal data")
ax.set_xlabel("value")
ax.set_ylabel("count")
ax.axvline(normal.mean(), color="red", linestyle="--", label="mean")
ax.legend()
plt.show()

# --- bins change the story ---------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), sharey=True)
for ax, bins in zip(axes, [5, 30, 100]):
    ax.hist(normal, bins=bins)
    ax.set_title(f"bins={bins}")  # too few hides detail; too many shows noise
fig.tight_layout()
plt.show()

# --- compare two distributions -----------------------------------------------
fig, ax = plt.subplots()
ax.hist(normal, bins=30, alpha=0.6, label="normal")
ax.hist(skewed, bins=30, alpha=0.6, label="skewed")  # alpha = transparency
ax.set_title("Two distributions")
ax.legend()
plt.show()

# --- box plot: median, quartiles, and outliers in a compact form -------------
fig, ax = plt.subplots()
ax.boxplot([normal, skewed], tick_labels=["normal", "skewed"])
ax.set_title("Box plot")
ax.set_ylabel("value")
plt.show()
# Box = middle 50% of data, line = median, whiskers = typical range, dots = outliers.

# --- from a pandas column ----------------------------------------------------
# import pandas as pd
# df["latency_ms"].plot.hist(bins=20)    # pandas has plotting built on matplotlib
# plt.show()

# --- numbers that go with the picture ----------------------------------------
print("normal  mean/median:", round(normal.mean(), 2), round(np.median(normal), 2))
print("skewed  mean/median:", round(skewed.mean(), 2), round(np.median(skewed), 2))
# Skewed data: the mean is pulled toward the long tail, so mean > median.

# Why this matters in AI/ML: check feature distributions before training,
# spot outliers, compare prediction scores, and see whether classes are balanced.
