"""Tensors: what they are, how to create them, and how to read their shape.

Install first (inside your venv), CPU version:
    python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
(For a GPU build, pick your command at https://pytorch.org/get-started/locally/)
"""

import numpy as np
import torch

# =============================================================================
# WHAT EXACTLY IS A TENSOR?
# =============================================================================
# A tensor is a container of numbers arranged along zero or more axes, where
# every number has the same type. That is all.
#   0 axes -> scalar   (one number)
#   1 axis -> vector   (a list of numbers)
#   2 axes -> matrix   (a table)
#   3+ axes -> "higher" tensors (a stack of tables, a batch of images...)
# It is the NumPy array you already know, with two superpowers:
#   1. it can live on a GPU (many numbers processed in parallel)
#   2. it can remember how it was computed, so PyTorch can find gradients
#      automatically (autograd.py). That is how neural networks learn.
# The shape is its meaning: shape (32, 3, 224, 224) read as
#   "32 images, 3 color channels, 224 high, 224 wide".

scalar = torch.tensor(5.0)
vector = torch.tensor([1.0, 2.0, 3.0])
matrix = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
batch_of_images = torch.zeros(32, 3, 224, 224)  # a 4-axis tensor

for name, t in [("scalar", scalar), ("vector", vector), ("matrix", matrix), ("images", batch_of_images)]:
    print(f"{name:7} ndim={t.ndim} shape={tuple(t.shape)} numel={t.numel()}")

# --- creating tensors --------------------------------------------------------
print(torch.zeros(2, 3))
print(torch.ones(2, 2))
print(torch.arange(0, 10, 2))  # like range()
print(torch.linspace(0, 1, 5))
print(torch.eye(3))
torch.manual_seed(42)  # seed = reproducible random numbers
print(torch.rand(2, 3))  # uniform in [0, 1)
print(torch.randn(2, 3))  # normal: mean 0, std 1
print(torch.zeros_like(matrix))  # same shape and type as another tensor

# --- dtype: the number type, and why float32 -------------------------------
print(torch.tensor([1, 2, 3]).dtype)  # torch.int64  (whole numbers)
print(torch.tensor([1.0, 2.0]).dtype)  # torch.float32 (the default for decimals)
print(torch.tensor([1, 2, 3]).float().dtype)  # convert with .float(), .long(), .to(dtype)
# Neural networks use float32: precise enough, fast, and half the memory of float64.
# Gotcha: integer tensors can't hold gradients, and mixing dtypes can raise errors.

# --- shape tools -------------------------------------------------------------
numbers = torch.arange(12)
print(numbers.reshape(3, 4).shape)  # torch.Size([3, 4])
print(numbers.reshape(2, -1).shape)  # -1: work it out -> (2, 6)
print(numbers.reshape(3, 4).T.shape)  # transpose -> (4, 3)
print(torch.zeros(3, 1).squeeze().shape)  # remove size-1 axes -> (3,)
print(torch.zeros(3).unsqueeze(0).shape)  # add an axis at position 0 -> (1, 3)
# Almost every PyTorch error is a shape mismatch: print .shape often.

# --- indexing and slicing: same as NumPy -------------------------------------
print(matrix[0])  # first row
print(matrix[:, 1])  # second column
print(matrix[matrix > 2])  # boolean mask
print(matrix[1, 2].item())  # .item() turns a one-number tensor into a Python float

# --- NumPy and Python interop ------------------------------------------------
array = np.array([1.0, 2.0, 3.0])
from_numpy = torch.from_numpy(array)  # shares memory with the array
back_to_numpy = vector.numpy()  # CPU tensors only
print(from_numpy, back_to_numpy)
print(matrix.tolist())

# Next: tensor_operations.py (math), cpu_vs_gpu.py (devices), autograd.py (learning).
