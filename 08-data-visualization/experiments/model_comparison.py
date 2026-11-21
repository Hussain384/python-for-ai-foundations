"""Comparing experiment results: bar charts, grouped bars, and a confusion matrix."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- results of a few experiments, as a DataFrame ----------------------------
results = pd.DataFrame(
    {
        "model": ["alpha", "beta", "gamma", "alpha", "beta", "gamma"],
        "dataset": ["v1", "v1", "v1", "v2", "v2", "v2"],
        "accuracy": [0.91, 0.87, 0.95, 0.93, 0.82, 0.96],
        "latency_ms": [142, 187, 99, 131, 205, 110],
    }
)

# --- bar chart of the average per model --------------------------------------
average = results.groupby("model")["accuracy"].mean().sort_values(ascending=False)

fig, ax = plt.subplots()
ax.bar(average.index, average.values, color="tab:blue")
for position, value in enumerate(average.values):
    ax.text(position, value + 0.002, f"{value:.3f}", ha="center")  # label each bar
ax.set_title("Average accuracy by model")
ax.set_ylabel("accuracy")
ax.set_ylim(0.8, 1.0)
plt.show()

# --- grouped bars: models side by side for each dataset ----------------------
table = results.pivot(index="model", columns="dataset", values="accuracy")  # rows=model, cols=dataset
table.plot.bar(rot=0)  # pandas draws it with matplotlib
plt.title("Accuracy by model and dataset")
plt.ylabel("accuracy")
plt.ylim(0.7, 1.0)
plt.tight_layout()
plt.show()

# --- accuracy vs speed: the trade-off every team faces -----------------------
fig, ax = plt.subplots()
ax.scatter(results["latency_ms"], results["accuracy"])
for _, row in results.iterrows():
    ax.annotate(f"{row['model']}-{row['dataset']}", (row["latency_ms"], row["accuracy"]))
ax.set_title("Accuracy vs latency (top-left is best)")
ax.set_xlabel("latency (ms)")
ax.set_ylabel("accuracy")
plt.show()

# --- confusion matrix: where a classifier makes mistakes ---------------------
labels = ["cat", "dog", "bird"]
matrix = np.array(
    [
        [50, 3, 2],  # true cats:  50 predicted cat, 3 dog, 2 bird
        [4, 45, 1],  # true dogs
        [2, 2, 41],  # true birds
    ]
)

fig, ax = plt.subplots()
image = ax.imshow(matrix, cmap="Blues")  # a matrix shown as colored squares
fig.colorbar(image)
ax.set_xticks(range(len(labels)), labels=labels)
ax.set_yticks(range(len(labels)), labels=labels)
ax.set_xlabel("predicted")
ax.set_ylabel("true")
ax.set_title("Confusion matrix")
for row in range(3):
    for col in range(3):
        ax.text(col, row, matrix[row, col], ha="center", va="center")  # numbers in cells
plt.show()
print("overall accuracy:", round(np.trace(matrix) / matrix.sum(), 3))  # diagonal / total

# --- save a chart to the repo (images go in a folder, not next to the code) --
output_dir = Path(__file__).resolve().parent / "output"
output_dir.mkdir(exist_ok=True)
fig, ax = plt.subplots()
ax.bar(average.index, average.values)
fig.savefig(output_dir / "model_accuracy.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("saved", output_dir / "model_accuracy.png", "(add output/ to .gitignore if you don't commit images)")
