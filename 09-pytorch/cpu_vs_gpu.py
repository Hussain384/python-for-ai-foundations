"""CPU vs GPU: where a tensor lives and how to move it."""

import time

import torch

# --- why a GPU? --------------------------------------------------------------
# A CPU has a few powerful cores; a GPU has thousands of simple ones.
# Neural-network math is huge numbers of independent multiply-adds, which a GPU
# does in parallel. Small tasks can be faster on a CPU (copying data costs time).

# --- find the best available device ------------------------------------------
if torch.cuda.is_available():  # NVIDIA GPU
    device = torch.device("cuda")
elif torch.backends.mps.is_available():  # Apple Silicon GPU
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print("using device:", device)
# This works on any machine, so the same script runs with or without a GPU.

# --- every tensor lives on exactly one device --------------------------------
x = torch.rand(3, 3)
print(x.device)  # cpu (the default)
x = x.to(device)  # .to() returns a NEW tensor on that device; assign it
print(x.device)

# --- the classic error: mixing devices ---------------------------------------
cpu_tensor = torch.rand(2)
gpu_tensor = torch.rand(2, device=device)
if device.type != "cpu":
    try:
        cpu_tensor + gpu_tensor
    except RuntimeError as error:
        print("RuntimeError: tensors on different devices")
# Rule: model, inputs, and targets must all be on the same device.

# --- create directly on the device (faster than creating then moving) --------
y = torch.zeros(2, 2, device=device)

# --- back to CPU for NumPy, printing, or plotting ----------------------------
as_numpy = y.cpu().numpy()  # .numpy() only works on CPU tensors
print(as_numpy.shape)

# --- speed comparison: a big matrix multiplication ---------------------------
size = 2000
a = torch.rand(size, size)
b = torch.rand(size, size)

start = time.perf_counter()
a @ b
print(f"CPU: {time.perf_counter() - start:.3f}s")

if device.type == "cuda":
    a_gpu, b_gpu = a.to(device), b.to(device)
    torch.cuda.synchronize()  # GPU work is asynchronous; wait before timing
    start = time.perf_counter()
    a_gpu @ b_gpu
    torch.cuda.synchronize()
    print(f"GPU: {time.perf_counter() - start:.3f}s")
else:
    print("no CUDA GPU here; that is fine for learning (everything works on CPU)")

# The device pattern you will use in every training script:
#   device = ...                      (as above)
#   model = model.to(device)
#   for inputs, targets in loader:
#       inputs, targets = inputs.to(device), targets.to(device)
