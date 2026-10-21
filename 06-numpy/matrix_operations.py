"""Matrix operations: the math behind neural-network layers."""

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# --- element-wise vs matrix multiplication -----------------------------------
print(A * B)  # element-wise: [[ 5 12] [21 32]]
print(A @ B)  # matrix multiplication: [[19 22] [43 50]]

# Matrix multiplication rule: (m, n) @ (n, p) -> (m, p). Inner sizes must match.
x = np.array([[1, 2, 3]])  # (1, 3)
W = np.ones((3, 2))  # (3, 2)
print((x @ W).shape)  # (1, 2)
try:
    W @ x  # (3, 2) @ (1, 3): 2 != 1
except ValueError as error:
    print("ValueError: shapes don't line up")

# --- transpose: swap rows and columns ----------------------------------------
print(A.T)
print(np.arange(6).reshape(2, 3).T.shape)  # (2, 3) -> (3, 2)

# --- identity, inverse, determinant ------------------------------------------
I = np.eye(2)
print(A @ I)  # multiplying by identity changes nothing
print(np.linalg.inv(A))  # inverse
print(np.linalg.det(A))  # determinant: about -2.0 (float rounding)
print(np.round(A @ np.linalg.inv(A), 6))  # back to the identity

# --- solving a system of equations: 2x + y = 5 and x + 3y = 10 --------------
coefficients = np.array([[2, 1], [1, 3]])
results = np.array([5, 10])
print(np.linalg.solve(coefficients, results))  # [1. 3.]

# --- one neural-network layer: output = input @ weights + bias ---------------
rng = np.random.default_rng(0)
batch = rng.random((4, 3))  # 4 samples, 3 features each
weights = rng.random((3, 2))  # maps 3 features -> 2 outputs
bias = np.array([0.1, -0.1])  # shape (2,) broadcasts across the 4 samples
output = batch @ weights + bias
print(output.shape)  # (4, 2)

# This single line (shapes, @, broadcasting) is the core of deep learning.
