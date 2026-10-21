"""Broadcasting: NumPy stretches smaller arrays so different shapes can combine."""

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2, 3)

# --- scalar + matrix: the scalar is stretched to every element ---------------
print(matrix + 10)

# --- vector + matrix: the row is stretched down every row --------------------
row = np.array([10, 20, 30])  # shape (3,)
print(matrix + row)  # (2, 3) + (3,) -> (2, 3)

# --- column vector + matrix: the column is stretched across every column -----
column = np.array([[100], [200]])  # shape (2, 1)
print(matrix + column)  # (2, 3) + (2, 1) -> (2, 3)

# --- the rule ----------------------------------------------------------------
# Compare shapes from the RIGHT. Two sizes are compatible if they are equal or
# one of them is 1 (a missing size counts as 1). Size 1 is stretched to match.
#   (2, 3) and (3,)   -> OK:  (3,) acts like (1, 3)
#   (2, 3) and (2, 1) -> OK:  the 1 is stretched to 3
#   (2, 3) and (2,)   -> ERROR: 3 vs 2
try:
    matrix + np.array([1, 2])
except ValueError as error:
    print("ValueError:", error)

# --- real use: normalize each column of a dataset ----------------------------
data = np.array([[170.0, 65.0], [180.0, 80.0], [160.0, 50.0]])  # height, weight
mean = data.mean(axis=0)  # shape (2,): one mean per column
std = data.std(axis=0)
print((data - mean) / std)  # (3, 2) - (2,) broadcasts across every row

# --- reshape to control which way it stretches -------------------------------
v = np.array([1, 2, 3])
print(v.reshape(3, 1) + v)  # (3, 1) + (3,) -> (3, 3) table of sums
print(v[:, np.newaxis].shape)  # np.newaxis adds an axis -> (3, 1)
