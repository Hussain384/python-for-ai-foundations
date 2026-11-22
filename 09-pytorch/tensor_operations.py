"""Tensor operations: math, matrix multiplication, broadcasting, reductions.

If you did phase 06 (NumPy), most of this is the same with torch instead of np.
"""

import torch

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# --- element-wise ------------------------------------------------------------
print(a + b, a * b, a**2, a * 10)
print(torch.sqrt(a), torch.exp(a), torch.log(b))
print(a > 1.5)  # boolean tensor

# --- dot product and matrix multiplication -----------------------------------
print(a @ b)  # dot product -> tensor(32.)
x = torch.rand(4, 3)  # 4 samples, 3 features
W = torch.rand(3, 2)  # weights: 3 features -> 2 outputs
print((x @ W).shape)  # (4, 3) @ (3, 2) -> (4, 2)
# Rule: (m, n) @ (n, p) -> (m, p). The inner sizes must match.

# --- broadcasting: same rule as NumPy ----------------------------------------
bias = torch.tensor([0.1, -0.1])  # shape (2,)
print((x @ W + bias).shape)  # bias stretches across all 4 rows -> (4, 2)
# This line, inputs @ weights + bias, is one neural-network layer.

# --- reductions: collapse along a dimension ----------------------------------
scores = torch.tensor([[80.0, 90.0, 70.0], [60.0, 75.0, 95.0]])  # (2, 3)
print(scores.sum(), scores.mean())
print(scores.sum(dim=0))  # collapse rows    -> shape (3,)
print(scores.mean(dim=1))  # collapse columns -> shape (2,)
print(scores.max(dim=1))  # values and indices
print(scores.argmax(dim=1))  # position of the max in each row (class predictions)
# PyTorch says `dim` where NumPy says `axis`. Same idea: that dimension disappears.

# --- normalize each column (broadcasting + reductions) -----------------------
data = torch.tensor([[170.0, 65.0], [180.0, 80.0], [160.0, 50.0]])
print((data - data.mean(dim=0)) / data.std(dim=0))

# --- combining tensors -------------------------------------------------------
print(torch.cat([a, b]))  # join along an existing dimension -> shape (6,)
print(torch.stack([a, b]))  # make a NEW dimension -> shape (2, 3)

# --- activation functions: used between layers -------------------------------
z = torch.tensor([-2.0, -0.5, 0.0, 1.0, 3.0])
print(torch.relu(z))  # negatives -> 0
print(torch.sigmoid(z))  # squashes to (0, 1)
print(torch.softmax(z, dim=0))  # turns scores into probabilities that sum to 1

# --- in-place operations end with _ ------------------------------------------
t = torch.zeros(3)
t.add_(1)  # changes t itself
print(t)
# Avoid in-place ops on tensors that need gradients; they can break autograd.
