"""Indexing and slicing: pick out elements, rows, columns, and sub-arrays."""

import numpy as np

vector = np.array([10, 20, 30, 40, 50])
matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)

# --- indexing (same idea as lists, starts at 0, negatives count from the end) -
print(vector[0], vector[-1])  # 10 50
print(matrix[1, 2])  # row 1, column 2 -> 6   (list style matrix[1][2] also works)

# --- slicing: start:stop:step, stop is excluded ------------------------------
print(vector[1:4])  # [20 30 40]
print(vector[::2])  # [10 30 50]
print(vector[::-1])  # reversed

# --- slicing a matrix: matrix[rows, columns] ---------------------------------
print(matrix[0])  # first row     -> [1 2 3]
print(matrix[:, 0])  # first column  -> [1 4 7]
print(matrix[0:2, 1:3])  # top-right 2x2 block -> [[2 3] [5 6]]
print(matrix[-1, :])  # last row

# --- boolean masks: filter by condition (very common in data work) -----------
scores = np.array([0.2, 0.9, 0.5, 0.95, 0.1])
mask = scores > 0.4
print(mask)  # [False  True  True  True False]
print(scores[mask])  # [0.9  0.5  0.95]
print(scores[scores > 0.4])  # same, in one step

# --- fancy indexing: pick by a list of positions -----------------------------
print(vector[[0, 2, 4]])  # [10 30 50]

# --- assigning through an index or mask --------------------------------------
copy = scores.copy()
copy[copy < 0.3] = 0  # set low scores to 0
print(copy)

# --- GOTCHA: a slice is a VIEW, not a copy -----------------------------------
# Changing the slice changes the original. (Python list slices are copies.)
view = vector[1:3]
view[0] = 999
print(vector)  # [ 10 999  30  40  50]
safe = vector[1:3].copy()  # use .copy() when you need an independent array
