"""Aggregation (sum, mean, ...) along axes, and random numbers."""

import numpy as np

scores = np.array(
    [
        [80, 90, 70],  # student 0
        [60, 75, 95],  # student 1
    ]
)  # shape (2, 3): 2 students x 3 subjects

# --- aggregate everything ----------------------------------------------------
print(scores.sum(), scores.mean(), scores.min(), scores.max())

# --- aggregate along an axis: the axis you name is the one that disappears ---
print(scores.sum(axis=0))  # collapse rows    -> per subject: [140 165 165]
print(scores.sum(axis=1))  # collapse columns -> per student: [240 230]
print(scores.mean(axis=1))  # average per student
print(scores.shape, "->", scores.sum(axis=0).shape)  # (2, 3) -> (3,)

# --- other aggregations ------------------------------------------------------
print(scores.std(), np.median(scores))
print(scores.argmax(), scores.argmax(axis=1))  # position of the max (overall / per row)
print(scores.max(axis=1, keepdims=True).shape)  # keepdims keeps the axis -> (2, 1)

# --- random numbers ----------------------------------------------------------
# Use a Generator with a seed so results are reproducible (important in ML experiments).
rng = np.random.default_rng(seed=42)

print(rng.random(3))  # 3 floats in [0, 1)
print(rng.integers(0, 10, size=5))  # 5 ints from 0 to 9
print(rng.normal(loc=0, scale=1, size=3))  # bell curve: mean 0, std 1
print(rng.random((2, 3)))  # random matrix: this is how weights are initialised

items = np.array(["a", "b", "c", "d"])
print(rng.choice(items, size=2, replace=False))  # random sample
print(rng.permutation(5))  # shuffled 0..4 (used to shuffle a dataset)

# Same seed -> same numbers every run:
print(np.random.default_rng(1).random(2), np.random.default_rng(1).random(2))
