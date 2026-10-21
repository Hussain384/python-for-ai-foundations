"""Vector operations: math on whole arrays at once, no loops."""

import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])

# --- element-wise: operate on matching positions -----------------------------
print(a + b)  # [5. 7. 9.]
print(a * b)  # [ 4. 10. 18.]
print(a**2)  # [1. 4. 9.]
print(a * 10)  # scalar applies to every element

# --- math functions apply to every element -----------------------------------
print(np.sqrt(a))
print(np.exp(a))
print(np.log(b))

# --- comparison returns booleans ---------------------------------------------
print(a > 1.5)  # [False  True  True]
print(np.where(a > 1.5, "big", "small"))

# --- dot product: multiply matching elements, then add -----------------------
print(np.dot(a, b))  # 1*4 + 2*5 + 3*6 = 32.0
print(a @ b)  # same, with the @ operator

# --- vector length and distance ----------------------------------------------
print(np.linalg.norm(a))  # length of a: sqrt(1+4+9)
print(np.linalg.norm(a - b))  # distance between a and b

# --- cosine similarity: how similar two directions are (used for embeddings) -
cosine = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(round(float(cosine), 4))  # close to 1.0 = very similar

# --- why NumPy: vectorized code vs a Python loop -----------------------------
values = [1, 2, 3, 4]
print([v * 2 for v in values])  # loop: 4 separate Python operations
print(np.array(values) * 2)  # vectorized: one operation, runs in fast C code
# Rule: if you are writing a for-loop over array elements, look for a vectorized way.
