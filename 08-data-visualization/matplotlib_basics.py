"""Matplotlib basics: figure, axes, line / bar charts, labels, subplots, saving.

Install first (inside your venv):  python -m pip install matplotlib
Run the file: windows open one after another; close each window to see the next.
"""

import matplotlib.pyplot as plt
import numpy as np

# --- the two objects you need ------------------------------------------------
# Figure = the whole picture (the canvas).  Axes = one chart drawn on it.
# plt.subplots() gives you both. Draw on `ax`, then call plt.show().

# --- 1. line chart -----------------------------------------------------------
x = np.arange(1, 6)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Line chart")
ax.set_xlabel("x")
ax.set_ylabel("x squared")
plt.show()

# --- 2. style: markers, colors, line styles, legend --------------------------
fig, ax = plt.subplots()
ax.plot(x, x, marker="o", linestyle="--", color="tab:blue", label="x")
ax.plot(x, x**2, marker="s", color="tab:orange", label="x squared")
ax.set_title("Two lines with a legend")
ax.set_xlabel("x")
ax.set_ylabel("value")
ax.legend()  # uses each line's label=
ax.grid(True, alpha=0.3)
plt.show()

# --- 3. bar chart: compare categories ----------------------------------------
models = ["alpha", "beta", "gamma"]
accuracy = [0.91, 0.87, 0.95]

fig, ax = plt.subplots()
ax.bar(models, accuracy, color="tab:green")
ax.set_title("Accuracy by model")
ax.set_ylabel("accuracy")
ax.set_ylim(0.8, 1.0)  # a truncated axis exaggerates differences: be honest about it
plt.show()

# --- 4. subplots: several charts in one figure -------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns; size in inches
axes[0].plot(x, y)
axes[0].set_title("Line")
axes[1].bar(models, accuracy)
axes[1].set_title("Bar")
fig.suptitle("Two charts side by side")
fig.tight_layout()  # stops labels overlapping
plt.show()

# --- 5. saving a figure ------------------------------------------------------
fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig("line_chart.png", dpi=150, bbox_inches="tight")  # save BEFORE or instead of show()
plt.close(fig)  # free memory when you make many figures
print("saved line_chart.png (delete it if you don't need it)")

# Which chart for what:
#   line     -> change over time or steps (training curves)
#   bar      -> compare categories (models, datasets)
#   scatter  -> relationship between two numbers (scatter_plots.py)
#   histogram-> distribution of one number (distributions.py)
# Use ax.* methods (object style) rather than plt.* shortcuts; it scales to subplots.
