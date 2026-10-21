"""Arrays: scalar, vector, matrix, tensor, and the words shape / dimension / axis.

Install first (inside your venv):  python -m pip install numpy
"""

import numpy as np

# --- the four shapes of data -------------------------------------------------
scalar = np.array(5)  # a single number           -> 0 dimensions
vector = np.array([1, 2, 3])  # a list of numbers  -> 1 dimension
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # a table (rows x columns) -> 2 dimensions
tensor = np.zeros((2, 3, 4))  # a stack of matrices -> 3 dimensions (e.g. batch of images)

for name, a in [("scalar", scalar), ("vector", vector), ("matrix", matrix), ("tensor", tensor)]:
    print(f"{name:7} ndim={a.ndim} shape={a.shape} size={a.size}")

# --- the vocabulary ----------------------------------------------------------
# ndim  (dimension) = how many axes the array has
# shape             = the length of each axis, as a tuple: (rows, columns) = (2, 3)
# size              = total number of elements (product of the shape)
# axis              = one direction of the array: axis 0 = down the rows,
#                     axis 1 = across the columns, axis 2 = depth, ...
# Careful: a "3-dimensional vector" has shape (3,), which is 1 dimension (ndim=1).

# --- creating arrays ---------------------------------------------------------
print(np.zeros((2, 3)))  # all zeros
print(np.ones((2, 2)))  # all ones
print(np.full((2, 2), 7))  # all one value
print(np.arange(0, 10, 2))  # like range(): [0 2 4 6 8]
print(np.linspace(0, 1, 5))  # 5 evenly spaced numbers from 0 to 1
print(np.eye(3))  # identity matrix

# --- dtype: every element has the same type ----------------------------------
print(np.array([1, 2, 3]).dtype, np.array([1.5, 2, 3]).dtype)  # int64 float64
print(np.array([1, 2, 3], dtype=np.float32).dtype)  # float32 is common in deep learning

# --- reshape: same data, different shape -------------------------------------
numbers = np.arange(12)
print(numbers.reshape(3, 4))  # 3 rows, 4 columns
print(numbers.reshape(2, -1).shape)  # -1 = "work this one out" -> (2, 6)
print(numbers.reshape(3, 4).flatten().shape)  # back to 1-D -> (12,)

# --- NumPy array vs Python list ----------------------------------------------
# A list can mix types and is slow for math; an array holds one type and is fast.
print([1, 2, 3] * 2)  # list: repeats    -> [1, 2, 3, 1, 2, 3]
print(np.array([1, 2, 3]) * 2)  # array: math -> [2 4 6]
