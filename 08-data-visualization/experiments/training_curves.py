"""Training curves: how ML experiments are watched while a model learns.

Real training records one loss number per step (epoch). Here we fake it with
NumPy so you can learn to READ the plots before PyTorch (phase 09) produces them.
"""

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=1)
epochs = np.arange(1, 31)


def noisy(values, amount):
    return values + rng.normal(0, amount, size=len(values))


# --- a healthy run: both losses fall and stay close --------------------------
train_loss = noisy(2.0 * np.exp(-0.12 * epochs) + 0.20, 0.02)
val_loss = noisy(2.0 * np.exp(-0.11 * epochs) + 0.25, 0.03)

fig, ax = plt.subplots()
ax.plot(epochs, train_loss, label="train loss")
ax.plot(epochs, val_loss, label="validation loss")
ax.set_title("Healthy training")
ax.set_xlabel("epoch")
ax.set_ylabel("loss (lower is better)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()

# --- overfitting: train keeps improving, validation turns upward -------------
train_over = noisy(2.0 * np.exp(-0.2 * epochs) + 0.02, 0.01)
val_over = noisy(0.55 + 0.9 * np.exp(-0.25 * epochs) + 0.012 * np.maximum(epochs - 10, 0), 0.02)
best_epoch = int(np.argmin(val_over)) + 1

fig, ax = plt.subplots()
ax.plot(epochs, train_over, label="train loss")
ax.plot(epochs, val_over, label="validation loss")
ax.axvline(best_epoch, color="gray", linestyle="--", label=f"best epoch = {best_epoch}")
ax.set_title("Overfitting: validation loss rises while train loss keeps falling")
ax.set_xlabel("epoch")
ax.set_ylabel("loss")
ax.legend()
plt.show()
# The gap between the curves is the warning. Fixes: more data, regularization,
# a smaller model, or early stopping (stop at the best epoch).

# --- loss and accuracy side by side ------------------------------------------
accuracy = np.clip(noisy(1 - train_loss / 2.2, 0.01), 0, 1)
val_accuracy = np.clip(noisy(1 - val_loss / 2.2, 0.015), 0, 1)

fig, (ax_loss, ax_acc) = plt.subplots(1, 2, figsize=(11, 4))
ax_loss.plot(epochs, train_loss, label="train")
ax_loss.plot(epochs, val_loss, label="validation")
ax_loss.set_title("Loss")
ax_loss.set_xlabel("epoch")
ax_loss.legend()

ax_acc.plot(epochs, accuracy, label="train")
ax_acc.plot(epochs, val_accuracy, label="validation")
ax_acc.set_title("Accuracy")
ax_acc.set_xlabel("epoch")
ax_acc.legend()
fig.tight_layout()
plt.show()

# --- learning rate comparison: one line per experiment -----------------------
fig, ax = plt.subplots()
for lr, rate in [(0.001, 0.04), (0.01, 0.12), (0.1, 0.30)]:
    ax.plot(epochs, noisy(2.0 * np.exp(-rate * epochs) + 0.2, 0.02), label=f"lr={lr}")
ax.set_title("Comparing learning rates")
ax.set_xlabel("epoch")
ax.set_ylabel("loss")
ax.legend()
plt.show()

# How to read a training plot:
#   - loss going down      -> the model is learning
#   - flat from the start  -> learning rate too small, or a bug
#   - wild zig-zags        -> learning rate too large
#   - train down, val up   -> overfitting
#   - both high and flat   -> underfitting (model too simple)
