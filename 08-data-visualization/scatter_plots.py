"""Scatter plots: the relationship between two numbers, and between groups."""

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=0)

# --- a basic scatter: each dot is one row of data ----------------------------
hours = rng.uniform(0, 10, size=60)  # hours studied
score = 40 + 5 * hours + rng.normal(0, 6, size=60)  # score rises with hours, plus noise

fig, ax = plt.subplots()
ax.scatter(hours, score, alpha=0.7)
ax.set_title("Hours studied vs score")
ax.set_xlabel("hours")
ax.set_ylabel("score")
plt.show()

# --- add a trend line (a straight-line fit) ----------------------------------
slope, intercept = np.polyfit(hours, score, deg=1)  # best straight line
line_x = np.array([0, 10])

fig, ax = plt.subplots()
ax.scatter(hours, score, alpha=0.7)
ax.plot(line_x, slope * line_x + intercept, color="red", label=f"trend: slope={slope:.1f}")
ax.set_title("With a trend line")
ax.set_xlabel("hours")
ax.set_ylabel("score")
ax.legend()
plt.show()

# --- how strong is the relationship? correlation from -1 to 1 ----------------
print("correlation:", round(np.corrcoef(hours, score)[0, 1], 2))  # near 1 = strong upward
# Correlation does not prove one thing causes the other.

# --- color by group: classes in a classification problem ---------------------
class_a = rng.normal(loc=[2, 2], scale=0.8, size=(50, 2))  # 50 points around (2, 2)
class_b = rng.normal(loc=[5, 5], scale=0.8, size=(50, 2))  # 50 points around (5, 5)

fig, ax = plt.subplots()
ax.scatter(class_a[:, 0], class_a[:, 1], label="class A", alpha=0.7)
ax.scatter(class_b[:, 0], class_b[:, 1], label="class B", alpha=0.7)
ax.set_title("Two classes in feature space")
ax.set_xlabel("feature 1")
ax.set_ylabel("feature 2")
ax.legend()
plt.show()
# If you can separate the groups with a line, a simple model will work.
# This is the picture behind classification.

# --- color and size from data ------------------------------------------------
fig, ax = plt.subplots()
points = ax.scatter(hours, score, c=score, cmap="viridis", s=hours * 10 + 10)
fig.colorbar(points, label="score")  # legend for the color scale
ax.set_title("Color and size carry extra information")
plt.show()

# --- actual vs predicted: the classic regression check -----------------------
actual = score
predicted = slope * hours + intercept

fig, ax = plt.subplots()
ax.scatter(actual, predicted, alpha=0.7)
low, high = actual.min(), actual.max()
ax.plot([low, high], [low, high], color="red", linestyle="--", label="perfect")
ax.set_title("Actual vs predicted")
ax.set_xlabel("actual")
ax.set_ylabel("predicted")
ax.legend()
plt.show()
# Dots on the red line = perfect predictions; spread away from it = errors.
