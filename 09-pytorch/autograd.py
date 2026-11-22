"""Autograd: PyTorch finds gradients for you. This is how neural networks learn."""

import torch

# --- the idea ----------------------------------------------------------------
# A gradient tells you: "if I nudge this number up a tiny bit, how much does the
# result change, and in which direction?" Learning = repeatedly nudging weights
# in the direction that makes the error (loss) smaller.

# --- first gradient: y = x**2, so dy/dx = 2x ---------------------------------
x = torch.tensor(3.0, requires_grad=True)  # "track operations on this tensor"
y = x**2
y.backward()  # walk backwards through the computation
print(x.grad)  # tensor(6.) = 2 * 3

# --- gradients through several steps (the chain rule, done for you) ----------
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)
inputs = torch.tensor(4.0)
target = torch.tensor(10.0)

prediction = w * inputs + b  # 2*4 + 1 = 9
loss = (prediction - target) ** 2  # (9 - 10)^2 = 1
loss.backward()
print("loss:", loss.item())
print("dloss/dw:", w.grad.item())  # 2 * (9-10) * 4 = -8
print("dloss/db:", b.grad.item())  # 2 * (9-10)     = -2
# Negative gradient: increasing w would DECREASE the loss -> so move w up.

# --- one manual learning step ------------------------------------------------
learning_rate = 0.01
with torch.no_grad():  # don't track this update as part of the computation
    w -= learning_rate * w.grad  # step opposite to the gradient
    b -= learning_rate * b.grad
print("new w, b:", w.item(), b.item())

# --- gradients ACCUMULATE: reset them every step -----------------------------
a = torch.tensor(1.0, requires_grad=True)
for _ in range(3):
    (a * 2).backward()
print(a.grad)  # tensor(6.) not 2: three backward calls added up
a.grad.zero_()  # reset before the next step (optimizer.zero_grad() does this)

# --- gradient descent from scratch: fit y = 2x + 1 ---------------------------
torch.manual_seed(0)
xs = torch.linspace(-1, 1, 50)
ys = 2 * xs + 1 + torch.randn(50) * 0.1  # data with a little noise

w = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
for step in range(200):
    predictions = w * xs + b
    loss = ((predictions - ys) ** 2).mean()  # mean squared error
    loss.backward()
    with torch.no_grad():
        w -= 0.1 * w.grad
        b -= 0.1 * b.grad
    w.grad.zero_()
    b.grad.zero_()
    if step % 50 == 0:
        print(f"step {step:3d} loss={loss.item():.4f}")
print(f"learned w={w.item():.2f} (true 2), b={b.item():.2f} (true 1)")

# --- turning tracking off ----------------------------------------------------
with torch.no_grad():  # use when evaluating or predicting: faster, less memory
    print((w * xs + b).requires_grad)  # False
detached = (w * 2).detach()  # a copy that is cut off from the graph
# Use .detach() before .numpy() on a tensor that tracks gradients.

# The training loop in loss_and_optimizers.py automates exactly these steps:
#   predict -> loss -> backward -> update -> zero the gradients.
